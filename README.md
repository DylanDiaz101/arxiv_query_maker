# arXiv Research Article Email Sender

This project queries the **arXiv API** for research articles and automatically sends a list of 1-10 relevant articles (from the past month) to a specified recipient email.

### Features
- Fetches research articles based on specific search queries.
- Sends results via email using an automated cloud-based service.
- Runs on **PythonAnywhere** ([pythonanywhere.com](https://www.pythonanywhere.com/)).

### Example Use Case
"Every month, I want to query arXiv and return 1-10 articles related to **cognitive architectures** and **cognitive modeling/computational cognitive modeling."

### Search Queries
#### Cognitive Architecture Search Query
```python
url_architecture = (
    'http://export.arxiv.org/api/query?'
    'search_query=all:cognitive+AND+all:architecture&'
    'start=0&max_results=10&sortBy=lastUpdatedDate&sortOrder=descending'
)
```

#### Cognitive Modeling Search Query
This includes results for **"cognitive modeling"** OR **"computational cognitive modeling"**.
```python
url_modeling = (
    'http://export.arxiv.org/api/query?'
    'search_query=all:%22cognitive%20modeling%22+OR+all:%22computational%20cognitive%20modeling%22&'
    'start=0&max_results=10&sortBy=lastUpdatedDate&sortOrder=descending'
)
```

### Additional Resources
For more details on structuring search queries, refer to the [arXiv API Documentation](https://info.arxiv.org/help/api/basics.html).



