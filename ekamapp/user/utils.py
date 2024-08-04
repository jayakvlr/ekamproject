from flask import session,redirect,url_for
import time

def trigger_webhook():
        # Check if webhook triggered or 10 minutes passed
    webhook_triggered = session.get('webhook_triggered', False)
    if webhook_triggered:
        # Redirect to dashboard
        return redirect(url_for('users.dashboard'))
    
    # Check if 10 minutes have passed
    start_time = session.get('start_time', None)
    if start_time:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 600:  # 10 minutes in seconds
            return redirect(url_for('users.register'))