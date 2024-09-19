# Exploratory Data Analysis (EDA)<br> for customer loans at a Financial Institution

## Overview

- **CONTEXT**
<p>You currently work for a large financial institution, where managing loans is a critical component of business operations.</p>

<p>To ensure informed decisions are made about loan approvals and risk is efficiently managed, your task is to gain a comprehensive understanding of the loan portfolio data.</p>

- **TASK**
<p>Your responsibility is to <b>perform exploratory data analysis (EDA) on the loan portfolio</b>, using various statistical and data visualisation techniques to uncover patterns, relationships, and anomalies in the loan data.</p>
<p>This information will enable the <b>business</b> to make more informed <b>decisions about (1) loan approvals, (2) pricing, and (3) risk management</b>.</p>

- **LEARNING OUTCOME**
<p>By conducting exploratory data analysis on the loan data, you aim to gain a deeper understanding of the risk and return associated with the business' loans.</p>
<p>Ultimately, your goal is to improve the performance and profitability of the loan portfolio.</p>

## Credits
The knowledge contained in this repository was primarily taught by <a href='https://www.theaicore.com' > AiCore</a>, and I am immensely grateful to them for their teaching and support in my continous professional development.

## Table of contents
1. [Overview](#overview)
2. [Milestones](#milestones)
    - [2.1: Set up the environment](#21-set-up-the-environment)
      - [2.1.1 OS Terminal](#211-os-terminal)
      - [2.1.2 Conda Virtual Environment](#212-conda-virtual-environment)
      - [2.1.3 Git](#213-git)
      - [2.1.4 GitHub](#214-github)
    - [2.2: Extract the loans data from the cloud](#22-extract-the-loans-data-from-the-cloud)
      - [2.2.1 X](#221-X)
      - [2.2.2 X](#222-X)
      - [2.2.3 X](#223-X)
      - [2.2.4 X](#224-X)
      - [2.2.5 X](#225-X)
      - [2.2.6 X](#226-X)
      - [2.2.7 X](#227-X)
    - [2.3: Exploratory Data Analysis (EDA)](#23-exploratory-data-analysis-(eda))
      - [2.3.1 X](#231-X)
      - [2.3.2 X](#232-X)
    - [2.4: Analysis and Visualisation](#24-analysis-and-visualisation)
      - [2.4.1 X](#241-X)
      - [2.4.2 X](#242-X)
      - [2.4.3 X](#243-X)
      - [2.4.4 Refactor and optimise current code](#244-refactor-and-optimise-current-code)
    - [2.5: Putting it all together](#25-putting-it-all-together)
      - [2.5.1 X](#251-Xe)
    - [2.6: Wrapped up: Handover](#26-wrapped-up-handover-)
      - [2.6.1 Improvements: step by step](#261-improvements-step-by-step)
      - [2.6.2 New Functionalities](#262-new-functionalities)
      - [2.6.3 Known Issues](#263-known-issues)
3. [Installation](#installation-instructions)
4. [Usage](#usage-instructions)
5. [File Structure](#file-structure)
6. [License Information](#license-information)
7. [Demonstrated Skills](#demonstrated-skills)

# Milestones
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. In order to achieve developing this game, I categorised it in milestones, which each has a specific subset of chapters.

## 2.1: Set up the environment
The first step in setting up the environment was to navigate and create a new directory on my local machine using the OS terminal.

#### 2.1.1 OS Terminal
<p>This was done with the following zsh commands:</p>

```sh
cd /path/to/parent-directory
mkdir customer-finance-loans
cd customer-finance-loans
```

#### 2.1.2 Conda Virtual Environment
Next, I created and initialized a new Conda virtual environment. This helps manage dependencies and keep them isolated from other projects. I also needed to download essential packages, such as _Python_.

```sh
# Create a new Conda environment with Python.
# Here you can add the modules after the assigned name to the conda environment, which you would like to use for your specific project
conda create -n finance_loans python=3.8 pyyaml psycopg2 sqlalchemy pandas

# Activate the  created environment
conda activate finance-loans
```

#### 2.1.3 Git
To manage the project’s version control, I cloned the GitHub repository, initialized a Git repository and performed some basic Git operations.

```sh
# Clone the existing GitHub repository
git clone https://github.com/your-username/repository.git

# Initialize a new Git repository
git init

# Check the current status of the repository
git status

# Add all changes to staging
git add .

# Commit the changes with a message
git commit -m "Initial commit: Add cloned repo."
```

#### 2.1.4 GitHub
Finally, once I want to push the local repository to GitHub, to keep it backed up and share it with others, I write the following command:
```sh
# If you want to push your changes to a remote repository (like GitHub), you need to add the remote URL.
git push origin main
```

## 2.2: Extract the loans data from the cloud


#### 2.2.1 Initialise a class to extract the data



#### 2.2.2 Extract the data from the RDS database



#### 2.2.3 Familiarise yourself with the data

**Dataset schema**

- `id`: unique id of the loan
- `member_id`: id of the member to took out the loan
- `loan_amount`: amount of loan the applicant received
- `funded_amount`: The total amount committed to the loan at the point in time 
- `funded_amount_inv`: The total amount committed by investors for that loan at that point in time 
- `term`: The number of monthly payments for the loan
- `int_rate`: Interest rate on the loan
- `instalment`: The monthly payment owned by the borrower
- `grade`: LC assigned loan grade
- `sub_grade`: LC assigned loan sub grade
- `employment_length`: Employment length in years.
- `home_ownership`: The home ownership status provided by the borrower
- `annual_inc`: The annual income of the borrower
- `verification_status`: Indicates whether the borrowers income was verified by the LC or the income source was verified
- `issue_date:` Issue date of the loan
- `loan_status`: Current status of the loan
- `payment_plan`: Indicates if a payment plan is in place for the loan. Indication borrower is struggling to pay.
- `purpose`: A category provided by the borrower for the loan request.
- `dti`: A ratio calculated using the borrowerâ€™s total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrowerâ€™s self-reported monthly income.
- `delinq_2yr`: The number of 30+ days past-due payment in the borrower's credit file for the past 2 years.
- `earliest_credit_line`: The month the borrower's earliest reported credit line was opened
- `inq_last_6mths`: The number of inquiries in past 6 months (excluding auto and mortgage inquiries)
- `mths_since_last_record`: The number of months since the last public record.
- `open_accounts`: The number of open credit lines in the borrower's credit file.
- `total_accounts`: The total number of credit lines currently in the borrower's credit file
- `out_prncp`: Remaining outstanding principal for total amount funded
- `out_prncp_inv`: Remaining outstanding principal for portion of total amount funded by investors
- `total_payment`: Payments received to date for total amount funded
- `total_rec_int`: Interest received to date
- `total_rec_late_fee`: Late fees received to date
- `recoveries`: post charge off gross recovery
- `collection_recovery_fee`: post charge off collection fee
- `last_payment_date`: Last month payment was received
- `last_payment_amount`: Last total payment amount received
- `next_payment_date`: Next scheduled payment date
- `last_credit_pull_date`: The most recent month LC pulled credit for this loan
- `collections_12_mths_ex_med`: Number of collections in 12 months excluding medical collections
- `mths_since_last_major_derog`: Months since most recent 90-day or worse rating
- `policy_code`: publicly available policy_code=1 new products not publicly available policy_code=2
- `application_type`: Indicates whether the loan is an individual application or a joint application with two co-borrowers


## 2.3: Exploratory Data Analysis (EDA)

### 2.3.1 


## 2.4: Analysis and Visualisation

### 2.4.1 


## 2.5: Putting it all together

### 2.5.1 


## 2.6: Wrapped up: Handover

### 2.6.1 


## Installation Instructions



## Usage



## File Structure



## License Information



## Demonstrated Skills