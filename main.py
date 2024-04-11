from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Bot

# Define your Telegram bot token
TOKEN = ""
# Define your Telegram group ID
GROUP_ID = -1001234567890  # Replace with your group ID
# Function to save user details to a text file
def save_user_details(sender_name, sender_id):
    with open("user_details.txt", "a") as file:
        file.write(f"Name: {sender_name}, ID: {sender_id}\n")
# Function to handle normal messages
def message_handler(update, context):
    # Get sender's details
    sender_name = update.message.from_user.first_name
    sender_id = update.message.from_user.id
    # Save the user details to a text file
    save_user_details(sender_name, sender_id)
    # Send a message back to the sender
    update.message.reply_text("Thank you for your message!")
    send_direct_message(sender_id, direct_message)

def main():
    # Create an Updater and pass it your bot's token
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))    
    updater.start_polling()    
    updater.idle()

if __name__ == '__main__':
    main()
