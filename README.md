# Case Study- Predicting the success of a bank marketing campaign

### Report and code
Please refer to notebook [case_study.ipynb](case_study.ipynb).

### Rest API 
The notebook produces an ONNX model that can be further deployed in a flask app inside a docker container.

You can try running the app and calling the model as exemplified:
```
docker build -t case_study .
docker run -p 8080:8080 case_study

curl --location 'http://127.0.0.1:8080/predict' \
--header 'Content-Type: application/json' \
--data '[
 29,385, 4, 999, 0, 1.4, 93.444, -36.1, 4.968, 5228.1, false, false, false, false, false, false, false, false, true, false, false, false, true, false, false, false, false, false, false, true, false, false, false, false, true, false, false, false, true, false, false, false, false, false, false, false, false, false, true, false, false, true, false
]'
```