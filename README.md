# img_upload_backend
This repo constains the django code for the image upload site.

🌐 Front end (react) code - <a href="https://github.com/shwetanshu07/img_upload_frontend">checkout here</a>

## Working Demonstrations

📹 Authorisation and new user registration - https://drive.google.com/file/d/175xozZUdtVPkA0Oh1rObas2YtJfYMDSe/view?usp=share_link
- Authentication done through Token Authentication
- New user can register with a username and password
- Already existing users can login
- Users will be only able to see images uploaded by them

📹 Uploading an image - https://drive.google.com/file/d/1mEXr_sZ4OlcCljszr3EQntG5HsD8N8Tz/view?usp=share_link
- Every image has a required title and description field

📹 Deleting an image and displaying image in 4x4 grid - https://drive.google.com/file/d/1NMJ8KZjQyfIchO_IDzYcEXd6w0qIDojc/view?usp=share_link
- Every image can be deleted by its owner
- Each image is displayed in a 4x4 grid (16 items pagination). Initally the image and the title are displayed. User can click on show details to check the description of the image.

📹 Error checking - https://drive.google.com/file/d/1NUWCGFdOsB4hTBxWPH-nPpevXAwuMX6N/view?usp=share_link
- During login 
  - valid credentials
- During new user registration
  - username should not be taken already by another user
  - password and confirm password should match
- During image upload
  - title, description and image are required

## Additional Feature
Additional feature of downloading the uploaded image has been provided.
