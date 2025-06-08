import os

os.system("python data/synthetic_data_gen.py")
os.system("python database/setup_db.py")
os.system("python database/insert_data.py")
os.system("python models/train_linear_model.py")
os.system("python dashboard/app.py")
