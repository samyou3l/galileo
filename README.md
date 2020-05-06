# galileo
## Python FRED data side project

### Getting started
**TODO**

### Files
- **.env**: Defines environment variables (secrets, keys, etc.).
- **config.yml**: Config variables. Also currently defines the FRED series to pull, which maybe should live elsewhere.
- **requirements.txt**: **TODO** Package dependencies.

#### app
- **app.py**: Main entry and exit point to the app.
- **service.py**: Converts request into a response.
- **models.py**: Handles everything database related (connections, pulling series).
- **settings.py**: Currently just pulls in env variables. Might be superfluous.

### Resources:
- [GitHub markdown](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [FRED api docs](https://fred.stlouisfed.org/docs/api/fred/)
- [A useful Python FRED API (github.com/mortada/fredapi)](https://github.com/mortada/fredapi)
- [More mortada fred API examples](https://mortada.net/python-api-for-fred.html)
- [Another Python FRED API (github.com/avelkoski/FRB)](https://github.com/avelkoski/FRB)
- [Dash](https://dash.plotly.com)
- [Simple Flask webapp tutorial at medium.com/bhavaniravi](https://medium.com/bhavaniravi/build-your-1st-python-web-app-with-flask-b039d11f101c)
- [Simple webapp tutorial at realpython.com (not flask)](https://realpython.com/python-web-applications/)
- [A little bulkier tutorial on building a RESTful CRUD app with Flask and react at okta.com](https://developer.okta.com/blog/2018/12/20/crud-app-with-python-flask-react)