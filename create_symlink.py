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


def select_folder(entry):
    # 定义文件夹选择函数
    folder = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder)


# 创建选择文件夹按钮
tk.Button(root, text="选择文件夹", command=lambda: select_folder(folder1_entry)).grid(row=0, column=2, padx=10, pady=10)
tk.Button(root, text="选择文件夹", command=lambda: select_folder(folder2_entry)).grid(row=1, column=2, padx=10, pady=10)


def create_symlink():
    # 创建创建软链接按钮
    try:
        src = folder1_entry.get()
        dest = folder2_entry.get()
        A = os.path.basename(src)
        _dest = os.path.join(dest, A)
        os.symlink(src, _dest)
        result_label.config(text="软链接创建成功！", fg="green")
    except Exception as e:
        result_label.config(text=e, fg="red")
        raise e


tk.Button(root, text="创建软链接", command=create_symlink).grid(row=2, column=1, padx=10, pady=10)
# 创建结果标签
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=3, column=1, padx=10, pady=10)

# 运行主循环
root.mainloop()
