
# Install

```python
pip install -r requirements.txt
```


# Run the project
## Add new face
This script will turn on the main camera, and will try to find a face to store.
- It will ask for a name for the user
- It will take about 100 pictures of the face

```shell
python3 new_face.py
```

## Train the model
If at least one face has been added to the system, it is possible to train the model.

```shell
python3 training.py
```

## Face recognition
After the model has been traied, it is possible to run the main script (recognition) to find known faces in the system
```python
python3 recognition.py
```
