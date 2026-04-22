# Follow-up questions

## 1.  How far were you able to get with the exercise?
I was able to create a calculator that works fairly well (Although it was mostly generated with prompting.) It's not as advanced as something like Desmos, but it works for day-to-day calculations.

## 2.  What challenges did you encounter in the process?
I didn't really face any big challenges in the process as I was mostly just prompting, then making sure that the calculator atleast worked.

## 3.  If you were given unlimited time, what additional functionality would you include?

I would probably go through and look at how I would reduce the latency between the client and the server. However, I mostly left the calculation logic on the backend because the project description stated that you should include "any backend logic needed to perform the calculations". However, if it were me - I would probably take backend out of the picture and simply implement everything on the front-end. I would probably also go through and read the code more closely/comment on the functions to make reviews easier.

## 4.  If you used AI, please include all of your prompts and answer the following questions:
    -   What did the AI do well?
    -   What did the AI do poorly?
    -   For the places it did poorly, how did you change your approach
        to your prompts to improve its output?



<br>
<br>

**Prompt 1:** ```generate me a front end for a calculator app. Make it similar to that of the iphone calculator```

<br>

**Response:**

```
I’ll build a complete iPhone-style calculator UI directly in your current index.html, including layout, styling, and button interactions so it works immediately in the browser. I’m checking the existing file first, then I’ll replace it with a polished, mobile-friendly implementation.

Read memory

I’m reading the current index.html content now so I can safely apply a focused replacement without affecting anything else in the workspace.

Read index.html

I’m now writing a full single-file calculator app with iPhone-like visuals, hover/tap feedback, keyboard support, and working math logic so you can open it and use it right away.

Edited
index.html
I’ve finished the implementation and I’m quickly validating for any HTML/JS issues in index.html before handing it over.

Checked index.html, no problems found

Built a complete iPhone-style calculator frontend in index.html.

What it includes:

iPhone-like visual design:
Clean dark body, circular keys, gray utility buttons, orange operators, and a pill-shaped 0 key.
Fully working calculator logic:
AC, +/-, %, decimals, chained operations, equals, divide-by-zero handling, and formatted display values.
Keyboard support:
Number keys, + - * /, Enter/=, %, ., and Escape/Backspace for clear.
Responsive behavior:
Scales cleanly for mobile and desktop, with subtle load/tap animations.
If you want, I can also add a top status bar and home indicator to make it look even closer to the exact iPhone calculator UI.
```

<br>

**Review:**
The AI did a pretty good job overall with the UI and the calculation logic. The website was clean, and is nearly a 1:1 copy of Apple's UI design. However, the AI created everything inside of a single index.html file - likely because it was the only file I created - thus it decided that putting all of the web functionalities inside of a single file was fine. I decided to ask the AI to move the styling components into a CSS file and the calculation logic into a backend server.

------------------------------------------------------------------------

**Prompt 2:** ```create a css file for the styling. create a flask file for the backend - we'll move the calculation to the backend.```

<br>

**Response:**

```
I'll extract the CSS into a separate file, create a Flask backend for calculator operations, and update the HTML to use the external CSS and call the backend API.

Done! I've created a separated architecture for your calculator:

Files created:

styles.css — All the iPhone-style visual design (colors, layout, animations, responsive breakpoints)

app.py — Flask backend with:

/calculate endpoint → performs math operations (±, ×, ÷, +)
/format endpoint → formats numbers for display
/health endpoint → status check
CORS enabled for frontend requests
index.html — Updated frontend that:

Links to the external styles.css
Makes async API calls to Flask on http://localhost:5000 for calculations
Keeps all UI interactions and animations client-side

To run:

# Install Flask and CORS
pip install flask flask-cors

# Start the backend
python app.py

# Open index.html in your browser

The calculator now offloads all math to the backend while keeping the responsive UI and keyboard support intact.
```


<br>

**Review:**
The AI was able to correctly separate the front-end component, the styling-component, and the back-end logical component correctly. It does well at translating the logic from front-end to back-end. However, as we all know, AI is horrendously bad at testing its own code (which makes sense). If I spent more time - I would probably prompt it to create its own unit tests, so that it can run its own outputs and see what's being done correctly and incorrectly.