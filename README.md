# realtime-face-detection
Purpose : Detect and verify ATM users on-the-spot, replacing PINs with face authentication.

Tech stack : Python 3, OpenCV (Haar-/LBP-cascade + CNN embedding), NumPy, Tkinter GUI, SQLite.

Core flow :

    Camera stream → face detection → preprocessing (align/resize).

    Embedding via pre-trained deep model → compare to encrypted templates.

    Match ≥ threshold ⇒ grant access & log event; else trigger alert.

Security : Biometric data stored as salted, AES-encrypted vectors; transport secured with TLS.

 in this project I contributed to make GUI  using (Tkinter) : Simple dashboard to

    start/stop live detection,

    enroll new users (capture & label),

    view real-time match status,

    display audit logs.
