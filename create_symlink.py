'''
atuher: carlwhen(ciya)
email: kinghwaking@163.com
'''
import os
import tkinter as tk
from tkinter import filedialog

# 创建主窗口
root = tk.Tk()
root.title("软链接创建")

# 创建标签和输入框
tk.Label(root, text="源文件夹:").grid(row=0, column=0, padx=10, pady=10)
folder1_entry = tk.Entry(root, width=50)
folder1_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="目标文件夹:").grid(row=1, column=0, padx=10, pady=10)
folder2_entry = tk.Entry(root, width=50)
folder2_entry.grid(row=1, column=1, padx=10, pady=10)

# 定义文件夹选择函数
def select_folder(entry):
    folder = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder)


# 创建选择文件夹按钮
tk.Button(root, text="选择文件夹", command=lambda: select_folder(folder1_entry)).grid(row=0, column=2, padx=10, pady=10)
tk.Button(root, text="选择文件夹", command=lambda: select_folder(folder2_entry)).grid(row=1, column=2, padx=10, pady=10)

# 创建创建软链接按钮
def create_symlink():
    src = folder1_entry.get()
    dest = folder2_entry.get()
    if os.path.exists(src):
        if os.path.exists(dest):
            if os.listdir(dest):
                result_label.config(text="目标文件夹存非空", fg="red")
            else:
                os.remove(dest)
        os.symlink(src, dest)
        result_label.config(text="软链接创建成功！", fg="green")
    else:
        result_label.config(text="输入的文件夹路径不存在，请重新输入。", fg="red")

tk.Button(root, text="创建软链接", command=create_symlink).grid(row=2, column=1, padx=10, pady=10)

# 创建结果标签
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=3, column=1, padx=10, pady=10)

# 运行主循环
root.mainloop()
