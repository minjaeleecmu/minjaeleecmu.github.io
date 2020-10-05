##########
# Edit your personal data
website_title = "Minjae Lee, Ph.D.";
name = "Minjae Lee";
current_title = "Co-Founder of Gloovi Inc.";
summary_part_one = """
	I finished my Ph.D. in Computer Science from Stanford University in 2018. I was fortunate to be supported by Samsung Scholarship and Max Planck.
	I received Masters degree from Stanford University in 2017 majoring in Computer Science.
	I graduated from Carnegie Mellon University in 2012 majoring in Computer Science and minoring in Art.
""";
summary_part_two = """
	I worked in Oculus VR, eBay Inc., Microsoft Corporation, Apple Inc., Samsung SDS in the past.
""";
summary_part_three = """
	One of my past projects, EteRNA, was covered in <a href="https://www.nytimes.com/2011/01/11/science/11rna.html">New York Times</a>,
	<a href="https://www.cnn.com/2011/10/23/tech/innovation/foldit-game-science-poptech">CNN</a>,
	<a href="https://www.wired.com/2012/07/ff_rnagame/">Wired</a>, and
	<a href="https://www.wsj.com/articles/videogamers-are-recruited-to-fight-tuberculosis-and-other-ills-1462290212">Wall Street Journal</a>.
	You can read my thesis <a href="./thesis.pdf">here</a>.
""";
email_address = "mjlgg@alumni.stanford.edu";
email_display = "mjlgg at alumni dot stanford dot edu";
etc = "Lives in the Gloovi headquarter";
website_url = "https://minjaeleecmu.github.io";
picture_url = "https://minjaeleecmu.github.io/batman.jpg";
picture_path = "./batman.jpg";
item1_icon = "cv";
item1_color = "#E07070";
item1_name = "CV";
item1_url = "./cv.pdf";
item2_icon = "googlescholar";
item2_color = "#6B74C9";
item2_name = "Google Scholar";
item2_url = "https://scholar.google.com/citations?user=11YLSM8AAAAJ&hl=env";
item3_icon = "linkedin";
item3_color = "#6580B5";
item3_name = "LinkedIn";
item3_url = "https://www.linkedin.com/in/minjae-lee-ph-d-50561150";
item4_icon = "angellist";
item4_color = "#575469";
item4_name = "AngelList";
item4_url = "https://angel.co/u/minjae-lee-2";

##########
html_file = open("template/index.html", "rt");
html_data = html_file.read();
html_data = html_data.replace("{{TEMPLATE_WEBSITE_TITLE}}", website_title);
html_data = html_data.replace("{{TEMPLATE_NAME}}", name);
html_data = html_data.replace("{{TEMPLATE_CURRENT_TITLE}}", current_title);
html_data = html_data.replace("{{TEMPLATE_SUMMARY_PART_ONE}}", summary_part_one);
html_data = html_data.replace("{{TEMPLATE_SUMMARY_PART_TWO}}", summary_part_two);
html_data = html_data.replace("{{TEMPLATE_SUMMARY_PART_THREE}}", summary_part_three);
html_data = html_data.replace("{{TEMPLATE_EMAIL_ADDRESS}}", email_address);
html_data = html_data.replace("{{TEMPLATE_EMAIL_DISPLAY}}", email_display);
html_data = html_data.replace("{{TEMPLATE_ETC}}", etc);
html_data = html_data.replace("{{TEMPLATE_WEBSITE_URL}}", website_url);
html_data = html_data.replace("{{TEMPLATE_PICTURE_URL}}", picture_url);
html_data = html_data.replace("{{TEMPLATE_PICTURE_PATH}}", picture_path);
html_data = html_data.replace("{{TEMPLATE_ITEM1_ICON}}", item1_icon);
html_data = html_data.replace("{{TEMPLATE_ITEM1_COLOR}}", item1_color);
html_data = html_data.replace("{{TEMPLATE_ITEM1_NAME}}", item1_name);
html_data = html_data.replace("{{TEMPLATE_ITEM1_URL}}", item1_url);
html_data = html_data.replace("{{TEMPLATE_ITEM2_ICON}}", item2_icon);
html_data = html_data.replace("{{TEMPLATE_ITEM2_COLOR}}", item2_color);
html_data = html_data.replace("{{TEMPLATE_ITEM2_NAME}}", item2_name);
html_data = html_data.replace("{{TEMPLATE_ITEM2_URL}}", item2_url);
html_data = html_data.replace("{{TEMPLATE_ITEM3_ICON}}", item3_icon);
html_data = html_data.replace("{{TEMPLATE_ITEM3_COLOR}}", item3_color);
html_data = html_data.replace("{{TEMPLATE_ITEM3_NAME}}", item3_name);
html_data = html_data.replace("{{TEMPLATE_ITEM3_URL}}", item3_url);
html_data = html_data.replace("{{TEMPLATE_ITEM4_ICON}}", item4_icon);
html_data = html_data.replace("{{TEMPLATE_ITEM4_COLOR}}", item4_color);
html_data = html_data.replace("{{TEMPLATE_ITEM4_NAME}}", item4_name);
html_data = html_data.replace("{{TEMPLATE_ITEM4_URL}}", item4_url);

html_file.close();

html_file = open("index.html", "wt");
html_file.write(html_data);
html_file.close();
