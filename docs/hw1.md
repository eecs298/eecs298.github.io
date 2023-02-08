---
layout: spec
title: EECS 298 Homework 1
subtitle: Due 11:59 PM EST on Friday, February 17, 2022. 
sitemapOrder: 20
---

Homework 1: Ad Auctions
==========================
Due 11:59 PM EST on Friday, February 17, 2022. 

## Submission
This homework will consist of a written section with reflection questions and a programming section in Python. You will submit your work via Gradescope (linked from Canvas). On Gradescope, there are two assignments you will need to use to submit. Upload your written responses for Part 1 as a `.pdf` file to the `Homework 1: Written Responses` Gradescope assignment. It is required that you typeset your written responses in a document editor or a program like LaTeX. In addition, upload your code for Part 2 as `hw1.py` to the `Homework 1: Code Submission` Gradescope assignment. The code that you upload to Gradescope for Part 2 will be graded using an autograder. This autograder will consist of both public test cases, the results of which are visible upon each submission, and private test cases, the results of which will only be visible after the deadline for the assignment. You can submit your code as many times as you wish. You are free to work as a group on this assignment, but you must write your responses and code individually.

## Introduction
For this assignment, you will explore the systems and social harms associated with targeted online advertising using the Google Ads platform as a case study. You will investigate the tools Google Ads presents to advertisers for the creation of advertising campaigns, as well as the mechanism the platform uses to auction targeted keywords to advertisers. 

## Part 1: Creating a Predatory Ad Campaign
In this section, you will play the role of a prospective advertiser on the Google Ads platform. Google Ads is the largest online advertising platform in the world, and this service makes up the bulk of Google's revenue. As such, Google has the incentive and the means to wield an enormous amount of influence over the advertisement industry, and one facet of that influence begins in the tools they provide to advertisers to craft their own targeted marketing campaigns. Your goal in this section will be to envision and create a *malicious* company seeking to promote themselves on the Google Ads platform and use these tools to construct the most predatory, exploitative, highly targeted advertising campaign you can!  (This is for educational purposes only.) As you investigate these tools, keep an eye open for the ways Google directs and empowers those seeking to create marketing campaigns of this nature. We encourage you to be creative and curious! 

### Creating your company
First, sketch out some details about your company. Give your company a name and decide what product to promote. In what ways will this product or the promotion of this product be harmful? How will you target the vulnerable? In what ways might your advertising strategy take advantage of consumers? Your product might be a scam, be addictive, or unfairly target certain demographics. Before you continue, brainstorm some keywords or demographic details that your campaign might target.

### Using Google Ads
Once you have decided on these details, Go to https://ads.google.com/ and click `Start now`. Sign in with a Google account. You will be directed to Google's ad campaign creator. Here, click `Switch to Expert Mode` on the bottom of the page. You will be asked to provide information about your business name and website. These are both optional, so leave the fields empty and click `Next`. Click `Skip` on the next two pages. On the following page, you will be asked to specify the type of campaign you wish to create. Select the `Display` option and click `Next`. You see a navigation tree on the right-hand side of the next page. Select the `Targeting` item from this tree. This is the page that contains the tools that you will be using for this assignment. You will not need to proceed past this page or provide billing information at any point. Click `Add targeting` to see the tools at your disposal to target users with your ad campaign. You will be using the `Audience Segments`, `Demographics`, and `Keywords` tools. Click each of these to add them to the page. 

### Audience Segments
The `Audience Segments` tool allows advertisers to target certain details of user ad profiles. These ad profiles are automatically constructed by Google on a per-user basis with the use of browser cookies. Due to the wide reach of Google Ads services across the internet, these ad profiles can be developed to incredible specificity. Click `Browse` in the `Edit targeted segments` box to get an idea for the details these ad profiles can contain. Take a look at the `Detailed demographics`, `Affinity`, and `In-market and life events` categories and their subcategories. Once you have an idea for the types of available audience segments, you can also use the search feature to explore your options. There is some Javascript trickery with the search boxes on this page -- if your results do not appear after pressing the Enter key, click elsewhere on the page to make the results display. 

Answer the following short-response questions:

1. Select at least four audience segments to target with your campaign. Discuss what they were, why you chose them, and how their inclusion might be harmful.  What would be the harms, and to whom?

2. Identify at least two audience segments which surprised you with their inclusion.  Google uses various measurements to determine who belongs to which segment and which segment is likely to search for a given keyword.  Given your best guess on how Google might measure your two audience segments, what effects are these measurements likely to have? Describe any potential harms, using the terms we discussed in class.

### Demographics
The `Demographics` tool allows advertisers to fine-tune the demographic information of their targeted audience. Click the `Learn more` button in the infobox at the bottom of this tool to open the `About demographic targeting` flyout, where you can gain a deeper understanding of how this demographic information is determined and obtained from users, as well as some advice from Google on how to utilize these demographics. 

Answer the following short-response questions:

{:start="3"}
3. Why does Google provide access to fields such as `Gender`, `Age`, and `Parental status`? What benefits might targeting within these demographics give to advertisers? Provide an example. 

4. Read and briefly reflect on the information in the `About demographic targeting` flyout (particularly the `How Google determines demographic information` section). How does Google measure demographic variables?  What effects are these measurements likely to have? Describe any potential harms, using the terms we discussed in class.

5. Select the demographics you wish to target with your campaign. Discuss what demographics you chose, why you chose them, and how their inclusion introduces any potential harms.

### Keywords
The `Keywords` tool allows advertisers to select keywords to target with their campaign. When a page contains one of the keywords selected with this tool, the campaign's advertisements will be shown on that page. Google provides advertisers a search function under the `Get keyword ideas` tab to direct advertisers to keywords that may make their campaigns successful. Type in phrases related to your business in the `Enter your product or service` search box in this tab in order to get keyword recommendations from the system, as well as the relevancy of those keywords to your brand. Again, there is some Javascript trickery with the search boxes on this page -- if your results do not appear after pressing the Enter key, click elsewhere on the page to make the results display. Some phrases might not generate any results -- keep these in mind and explore until you find other phrases that do generate results.

Answer the following short-response questions:

{:start="6"}
6. Using the search box, select at least ten keywords to target with your campaign. Discuss what they were, why you chose them, and how their inclusion could be harmful.

7. Some phrases are hardcoded not to yield any keyword results in the search bar. It is likely that Google bans certain words from yielding results in order to curate the types of products and strategies advertisers can use Google's platform for. Find some phrases that do not return any results and discuss why Google may have chosen to ban them from the system.
   
8. What are the benefits and harms of Google's ability to influence their platform via choosing which keywords advertisers can use?

9. Open a private browsing window and disable any adblockers you use (you may want to log out of Google first). Google each of the keywords you selected. What advertisements do you see on these searches? Discuss which keywords returned advertisements, what companies were advertising on these keywords, and why these companies might have selected those specific keywords while creating their own campaigns. If none of your keywords return advertisements, discuss why this might be and attempt to find some related keywords that do yield advertisements when searched.

### Reflection
Once you have completed the above sections, screenshot your work in each of the tools on this page and attach them to your written report. This concludes your work with the Google Ads platform -- you do not need to proceed to the next page.  

Answer the following short-response questions:

{:start="10"}
10.  Describe the company you created, as well as why you made the decisions you did during the creation process.  What would be the effects and harms of the advertising campaign you designed if it were to be launched?

11.  In what ways did Google's tools enable you to materialize the harm your company presents to society?


## Part 2: Implementing a Keyword Auction

Google Ads uses a sealed-bid second-price auction system to match keywords with prospective advertisers on the platform. This system has two components. In a sealed-bid auction, bidders make their bids without any information about other bids. In a general second-price auction system, the highest bidder for an item is chosen as the winner -- however, that bidder will not pay the actual price they bidded. Instead, they will pay the price of the second-highest bid. This continues, with the runner-up being chosen as the second-highest bidder and paying the price of the third-highest bid. This process continues until the desired number of winners is selected. Your task is to implement a simulation of Google's sealed-bid second-price auction system.

### bids.csv
You are provided with a database, `bids.csv`, detailing bids by different companies for a variety of keywords. Each company is competing for multiple keywords in the hopes of displaying their ads on Google searches that contain those keywords. Companies bid in terms of Cost-Per-Click (CPC) -- the price they are willing to pay each time a user clicks on one of their ads associated with that keyword. Each row represents a single CPC bid by a company for a keyword. There are three columns: `Company`, containing the name of the company making the bid; `Keyword`, containing the word or phrase that the company is competing for; and `Bid`, the price that the company has indicated that they are willing to pay. For each keyword, you will select two companies, the winner and the runner-up, and determine the amount that they will pay in Cost-Per-Click according to the general second-price auction system.

### hw1.py
Your task is to write a Python program to process this database using the Python `csv` class and apply Google's auction system as described. Base your program on the sample code provided in the form of `hw1.py`. You will be tasked with implementing one class, `Bid`, and four functions: `processCSV`, `auctionKeyword`, and `secondPriceAuction`. The `Bid` class will be used to represent each bid in `bids.csv`. The `processCSV` function will process the information in `bids.csv` and return a dictionary, with keywords as keys and lists of `Bid` objects representing bids for those keywords as values. The `auctionKeyword` function will take a list of `Bid` objects for the same keyword as input and execute a general second-price auction, returning a list containing the two winning `Bid` objects, updated with the price they will pay according to the auction. The `secondPriceAuction` function will house your calls to the other two functions and organize your auctioning of each keyword. This function will return the results of each call to `auctionKeyword` stored in a dictionary with the keywords as keys. 

More information on the implementation of these functions is given in the documentation given in `hw1.py`. Your code will be graded with the help of an autograder, so your implementations will need to match the function signatures described in the documentation in the sample code exactly. The necessary files are available on Canvas under `Files` > `Homework 1`, or, if you rather, you can download [hw1.py here](https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/hw1.py) and [bids.csv here](https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/bids.csv). (Right-click > `Save As...` or download to your terminal via `wget`.)

The database `bids.csv` includes bids for racially coded names.  For more on this, see [Discrimination in Online Ad Delivery](https://dataprivacylab.org/projects/onlineads/1071-1.pdf) (Sweeney 2013).

### Reflection Questions

{:start="12"}
12. Using terms discussed in class, describe the components and properties of Google Ads (including both advertiser-facing sides, like the ad auction system and the campaign creation system, and consumer-facing sides) as a sociotechnical system.

13. Choose three unrelated keywords from the database of bids `bids.csv`. For each, describe how a company that wins this keyword might use it in a way that results in harm. How does the ad auction system make this harm easier or harder to perpetuate?
