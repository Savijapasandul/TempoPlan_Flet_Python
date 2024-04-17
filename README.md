# TempoPlan_Flet_Python
 
### RoomReservePro

#### Description:
RoomReservePro is a Python application designed to manage room reservations. It utilizes Supabase as the backend for storing and retrieving data. The application provides various functionalities for users:

#### Features:
- **User Authentication:**
  - Users can create accounts with email, password, and username.
  - Existing users can log in with their credentials.

- **Room Booking:**
  - Users can view available rooms.
  - Search functionality allows users to find rooms based on starting and ending times.
  - Rooms can be booked for specific time slots.
  - Users can view active, past, and cancelled bookings.

- **Settings:**
  - Users have settings for toggling between light and dark themes.
  - Account details and logout option are available in the settings.

- **Navigation:**
  - The app has a responsive UI with tabs for Active, Past, and Cancelled bookings.
  - Users can easily switch between different sections of the application.
  - A search bar is available for finding specific rooms.

#### How to Use:
1. **Home Page (/):**
   - Displays active, past, and cancelled bookings in separate tabs.
   - Users can expand each booking to view details and take actions.
   
2. **Search Page (/search):**
   - Search for available rooms based on starting and ending times.
   - Book rooms for specific time slots.
   - Each room listing includes a booking button for easy reservation.

3. **Notifications Page (/notifications):**
   - Provides information on upcoming or current bookings.
   - Users can quickly take actions on notifications.

4. **Login Page (/login):**
   - Log in with existing account details.
   - New users can sign up for an account.

5. **Create Account Page (/create_account):**
   - Register for a new account with email, password, and username.

6. **Settings Page (/settings):**
   - Toggle between light and dark themes.
   - View and update account details.
   - Log out of the application.

#### Technologies Used:
- **Python Libraries:**
  - flet (UI framework for creating Flutter-like interfaces)
  - os (for interacting with the operating system)
  - supabase (for interacting with the Supabase backend)
  - dotenv (for loading environment variables)

#### How to Run:
1. Ensure you have Python installed.
2. Install the required libraries:
   ```
   pip install flet supabase-python python-dotenv
   ```
3. Set up Supabase:
   - Create a Supabase project and obtain the URL and API key.
   - Set these values in a `.env` file:
     ```
     SUPABASE_URL=your_supabase_url
     SUPABASE_KEY=your_supabase_api_key
     ```
4. Run the Python script:
   ```
   python script_name.py
   ```
5. Access the application in your browser at `http://localhost:8000/`.

#### Note:
- This application requires a Supabase account and project for full functionality.
- Make sure to set up your Supabase environment variables correctly for the app to connect to the backend.

Feel free to reach out if you have any questions or need further assistance with RoomReservePro! 🏨✨