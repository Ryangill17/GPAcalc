ONTARIO UNIVERSITY GPA CALCULATOR

#### VIDEO DEMO: https://youtu.be/a35poDktZ9E

#### DESCRIPTION:

Ontario University GPA Calculator Project
This project is a comprehensive Ontario University GPA Calculator designed to accommodate the unique GPA calculation methods used by various universities across Ontario. Each university has its own grading scales, letter grade mappings, and GPA calculation techniques. To enhance the user experience, this project dedicates a page to each university, featuring custom branding and colors for seamless identification. Users can navigate to their desired university page either by searching via the search tab or by scrolling through the logos of each university, with each logo linking to the specific GPA calculator page for that institution.

Project Overview
The GPA Calculator project is organized into several key files, each fulfilling distinct roles in functionality, styling, and user experience. The structure of the project is designed for scalability, allowing easy addition of new universities in the future while ensuring a polished and user-friendly interface for current users.

Files and Functionalities
index.html
The index.html file serves as the homepage and is a crucial part of the project's functionality. This page allows users to navigate the university options by either scrolling through available university logos or using a search function to quickly find their university. When a user selects a logo, they are redirected to that university's specific GPA calculator page. The file uses HTML and CSS to create dropdown menus and links, with images representing each university. Importantly, the URLs for these images are fetched from a separate image.json file, streamlining the organization of the project by separating image data from the core HTML structure.

style.css
The style.css file is dedicated to styling each page within the project, contributing significantly to the project's visual appeal. This CSS file defines styling for various HTML elements like classes, tags, and headers to maintain a consistent and professional aesthetic across the platform. Additionally, it supports unique university branding on individual pages, matching colors and logos to each institution for a customized user experience.

app.py
The app.py file acts as the backend of the application, using Flask and Python to facilitate smooth routing and rendering of templates and images. This file essentially serves as the project's middleman, linking the index.html homepage with the specific GPA calculator pages for each university. The use of Flask in app.py provides the flexibility to render different templates for each university page, allowing for distinct functionality based on each university's grading system. Additionally, it loads image data from image.json, enhancing efficiency and modularity by keeping image URLs separate from the main code.

layout.html
The layout.html file serves as a base layout, utilizing HTML and Jinja2 to establish a simple, reusable layout for each university page. This layout reduces redundancy by eliminating the need to repeatedly copy and paste similar code for each university page. Within layout.html, table elements are used to create a structured layout for user input fields, where users can enter their grades and credits. These inputs are processed via JavaScript functions, enabling dynamic GPA calculation and row additions directly on the page. This layout also includes calculation buttons for ease of use, allowing users to calculate their GPA and add new rows as needed.

University-Specific HTML Files
Each university has a dedicated HTML file that extends layout.html but incorporates unique JavaScript code to accommodate each school’s grading system. These files contain the logic required to process grades and credits according to each university’s scale. Since Ontario universities have varied methods for translating grades to GPA points, each file contains JavaScript functions tailored to convert letter grades, percentages, and point-based grades according to the specific grading metrics of each institution. Users can calculate their GPA directly on these pages, with functions that handle specific grading logic, outputs, and row-adding functionality.

image.json
The image.json file contains URLs for each university's logo image, which are fetched by the index.html and app.py files. Separating image data into image.json helps reduce clutter in the main HTML and Python files and allows for easier updates if logos or image links need to be modified. This file is essential for maintaining the project's modular structure and enhances readability and maintainability.

Design Choices and Considerations
In building this GPA calculator, a few key design choices were considered to create a functional, user-friendly tool that reflects the individuality of each university's grading system. Firstly, the decision to dedicate a page to each university, complete with unique branding and color schemes, enhances user experience and promotes a sense of familiarity for students of each institution. This approach required careful planning and the use of Jinja2 templating to streamline the creation of multiple, similar pages, enabling efficient expansion for additional universities in the future.

The use of layout.html as a base template was another intentional design choice. By establishing a shared layout file, the project avoids repetitive code and allows for a standardized structure across all pages, which not only reduces development time but also ensures consistent user experience. This templating approach is complemented by university-specific HTML files that contain unique JavaScript functions to accommodate the diverse grading standards, maintaining both flexibility and accuracy in GPA calculations.

To further simplify code organization, image URLs were moved to a separate image.json file. This decision promotes a clean codebase and makes updates to university logos easy, as the data is decoupled from the main HTML and backend files. Additionally, using Flask as the routing framework provided an effective way to handle requests and render different templates based on user interaction, enhancing the project’s scalability.

Conclusion
This Ontario University GPA Calculator project combines functionality, scalability, and design, offering a customized tool that meets the unique needs of students from various universities. By dedicating pages to each university with specific branding, and accommodating the diverse grading scales in Ontario, this calculator provides an intuitive and tailored GPA calculation experience. Through careful file organization, templating, and the separation of visual assets, the project is both robust and easy to maintain, making it a valuable resource for Ontario students.

Key notes:

- CALCULATES THE GPA OF EVERY UNIVERSITUY IN ONTARIO
- DEDICATES A PAGE TO EACH UNIVERSITY AS THEY CLACULATE GRADES DIFFERENTLY
- EACH PAGE USES UNIQUE UNIVERSITY BRANDING A COLOURS TO MAKE THE PAGE SPECIAL TO THE USER
- YOU MAKE SEARCH UP YOUR UNIVERSITY THROUGH THE SEARCH TAB OR SCROLL THE THE LOGOS OF EACH UNIVERSITY WHICH A CLICK ON EACH LOGO LEADING TO THE SPECIFIC CALCULATOR WEBPAGE
- MY FIRST PIECE OF FUNCTIONALITY IS THE INDEX.HTML FILE WHICH IS THE FILE RELATED TO THE HOMEPAGE ALLOWNG FOR YOU TO SCROLL THROUGH UNIVERSITYS AND SEARCH. THIS FILE USES HTML AND SOME CSS PROPERTIES TO FORMULATE DROPDOWN MENUS USING LISTS AND IMAGE TAGS INSIDE LINK TAGS TO LEAD YOU TO THE WEBPAGE. THE URLS ALSO FETCH IMAGES AND LINKS TO WEBPAGES FROM A STATIC IMAGE.JSON FILE AND THE APP.PY FILE
- THE SECOND FILE IS MY STYLE.CSS THAT INCLUDES ALLOWING THE STYLING FOR EACH AND EVERY FILE IN THE PROJECT. IT CONTAINS CSS FOR CLASSES, TAGS, HEADERS, ETC TO PROVIDE THE BEST VISUAL APPEAL
- MY THIRD FILE IS THE APP.PY WHICH USES ROUTING TO GET THE SPECIFC FILES FOR EACH UNIVERSITY AND RENDERS TEMPLATES AND IMAGES. THIS IS THE MIDDLE MAN BETWEEN THE INDEX AND SPECIFC WEBPAGE FILES ALLOWING FOR FULL FUNCTIONALITY. THIS FILE ALSO ALLOWS ME TO USE FLASK AND PYTHON FOR MORE EFFICENCY.
- MY FOURTH FILE IS LAYOUT.HTML WHICH USES HTML AND JINJA2
  TO CREATE A SIMPLE LAYOUT FOR EACH SCHOOLS WEBPAGE ALLOWING FOR LESS COPY AND PASTING WHEN CREATING REPITIVE PAGES FOR EACH UNIVERSITY. THE PAGE USES THE SIMPLE TABLE TAGS TO CREATE A TABLE ALLOWING FOR INPUT OF GRADES AND CREDITS WHICH GET PROCESSED INTO JAVASCRIPT FUNCTIONS TO OUTPUT SPECIFIC GRADES. THIS FILE ALSO USES BUTTONS TO ALLOW FOR USER TO CALCULATE GPA AND ADD ROWS
- MY FIFTH GROUP OF FILES IS THE SPECIFIC HTML FILE FOR EACH UNIVERSITY. THESE FILES EXTEND THE LAYOUT.HTML FILE BUT CONTAIN ALL THE JAVASCRIPT CODE THAT PROCESSES THE GRADES AND CREDITS INPUTED. DUE TO ALL SCHOOLS HAVING DIFFERENT WAYS OF CALCULATING GRADES, THE CODE CONSISTS OF DIFFERENT GPA, GRADE LETTER, POINT GRADE, AND PERCENTAGE CALCULATIONS THAT ARE SPECIFC TO THE SCALE OF EACH SCHOOL. IT ALSO CONTAINS THE FUNCTIONALITY FOR EACH OUTPUT AND ADDROW FUNCTION OF EACH TABLE.
- LAST IS MY IMAGE.JSON FILE WHICH CONTAINS THE URLS FOR EACH IMAGE AS THESE LINKS CAN BE LONG ALLOWING FOR SIMPLICITY IN THE INDEX FILE
