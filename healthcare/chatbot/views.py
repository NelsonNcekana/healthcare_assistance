"""
Views for the Healthcare Assistant Chatbot.
"""
import openai
from django.conf import settings
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import HealthLog, MedicationReminder, VitalSign


# OpenAI client will be initialized in the function


def dashboard_view(request):
    """
    Dashboard view showing health logs, medication reminders, and vital signs.
    """
    # Get recent health logs (last 7 days)
    recent_logs = HealthLog.objects.filter(
        date_created__gte=timezone.now() - timedelta(days=7)
    ).order_by('-date_created')[:10]

    # Get active medication reminders
    active_medications = MedicationReminder.objects.filter(
        is_active=True
    ).order_by('medication_name')

    # Get recent vital signs (last 30 days)
    recent_vitals = VitalSign.objects.filter(
        date_recorded__gte=timezone.now() - timedelta(days=30)
    ).order_by('-date_recorded')[:5]

    # Calculate statistics
    total_logs = HealthLog.objects.count()
    active_meds_count = active_medications.count()
    critical_logs = HealthLog.objects.filter(severity='critical').count()

    # Get today's medication reminders
    today = timezone.now().date()
    todays_medications = active_medications.filter(
        start_date__lte=today,
        end_date__gte=today
    ) | active_medications.filter(
        start_date__lte=today,
        end_date__isnull=True
    )

    context = {
        'recent_logs': recent_logs,
        'active_medications': active_medications,
        'todays_medications': todays_medications,
        'recent_vitals': recent_vitals,
        'total_logs': total_logs,
        'active_meds_count': active_meds_count,
        'critical_logs': critical_logs,
        'today': today,
    }

    return render(request, 'chatbot/dashboard.html', context)


def chat_view(request):
    """
    Handles the chat page:
    - Gets user input
    - Sends it to OpenAI API
    - Returns AI response to template
    - Maintains chat history in session
    """
    if "chat_history" not in request.session:
        request.session["chat_history"] = []

    answer = None

    if request.method == "POST":
        user_question = request.POST.get("question", "").strip()

        if not user_question:
            answer = "Please enter a question."
        else:
            try:
                # Initialize OpenAI client
                if not settings.OPENAI_API_KEY:
                    raise ValueError("OpenAI API key not found in settings")
                
                client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
                
                # Prepare messages with system prompt
                messages = [
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful healthcare assistant. "
                            "Provide accurate, educational health "
                            "information. Always remind users to consult "
                            "healthcare professionals for medical advice. "
                            "Keep responses concise and clear."
                        ),
                    }
                ]

                # Add chat history and current question
                messages.extend(request.session["chat_history"])
                messages.append({"role": "user", "content": user_question})

                # Call OpenAI chat completion - optimized for speed
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages,
                    max_tokens=200,  # Shorter responses = faster
                    temperature=0.5,  # More focused responses
                )

                # Extract AI message
                answer = response.choices[0].message.content

                # Update chat history
                request.session["chat_history"].append(
                    {"role": "user", "content": user_question}
                )
                request.session["chat_history"].append(
                    {"role": "assistant", "content": answer}
                )
                request.session.modified = True

            except openai.AuthenticationError:
                error_msg = (
                    "❌ Authentication Error: Check your OpenAI API key."
                )
                request.session["chat_history"].append(
                    {"role": "user", "content": user_question}
                )
                request.session["chat_history"].append(
                    {"role": "assistant", "content": error_msg}
                )
                request.session.modified = True
            except openai.RateLimitError:
                error_msg = (
                    "💰 Quota exceeded: Please check your OpenAI billing."
                )
                request.session["chat_history"].append(
                    {"role": "user", "content": user_question}
                )
                request.session["chat_history"].append(
                    {"role": "assistant", "content": error_msg}
                )
                request.session.modified = True
            except openai.APITimeoutError:
                error_msg = "⏰ Request timed out. Please try again."
                request.session["chat_history"].append(
                    {"role": "user", "content": user_question}
                )
                request.session["chat_history"].append(
                    {"role": "assistant", "content": error_msg}
                )
                request.session.modified = True
            except openai.APIError as e:
                error_msg = f"⚠️ OpenAI API error: {str(e)}"
                request.session["chat_history"].append(
                    {"role": "user", "content": user_question}
                )
                request.session["chat_history"].append(
                    {"role": "assistant", "content": error_msg}
                )
                request.session.modified = True
            except (ValueError, KeyError, TypeError) as e:  # noqa: BLE001
                error_msg = f"❌ Configuration error: {str(e)}"
                request.session["chat_history"].append(
                    {"role": "user", "content": user_question}
                )
                request.session["chat_history"].append(
                    {"role": "assistant", "content": error_msg}
                )
                request.session.modified = True
            except Exception as e:  # noqa: BLE001
                error_msg = f"❌ Unexpected error: {str(e)}"
                request.session["chat_history"].append(
                    {"role": "user", "content": user_question}
                )
                request.session["chat_history"].append(
                    {"role": "assistant", "content": error_msg}
                )
                request.session.modified = True

    return render(
        request,
        "chatbot/chat.html",
        {
            "answer": answer,
            "chat_history": request.session.get("chat_history", []),
        },
    )


def clear_chat(request):
    """
    Clears chat history stored in the session.
    """
    if "chat_history" in request.session:
        del request.session["chat_history"]
    return redirect('chat')
