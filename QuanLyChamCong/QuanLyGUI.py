from tkinter import *
from tkinter import ttk
import database_manager
from customtkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import face_recognition, cv2 
import numpy as np

def QuanLyLayout(right_frame):
    center_frame = LabelFrame(right_frame, background="white", width=600, height=750)
    center_frame.grid(row=0,column=0,sticky="nsew")

    right_frame_qly = LabelFrame(right_frame, background='white', width=700, height=750)
    right_frame_qly.grid(row=0,column=1,sticky="nsew")

    '''right_frame.grid_columnconfigure(1, weight=1)
    right_frame.grid_columnconfigure(0, weight=2)
    right_frame.grid_rowconfigure(0, weight=1)'''


    # right_frame_qly

    '''style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview",
                    background="#D3D3D3",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#D3D3D3")

    # Change selected color
    style.map('Treeview', background=[('Selected', "lightblue")])'''

    timKiem_frame = Frame(right_frame_qly, background="white")
    timKiem_frame.pack(pady=10)
    lb_timkiem = Label(timKiem_frame, text="Tìm kiếm theo:", font=("Helvetica", 15), foreground="red", background="white")
    lb_timkiem.grid(row=0, column=0, padx= 5, pady=10)
    value_timkiem = ["Mã nhân viên", "Tên nhân viên", "Chức vụ"]
    cb_timkiem = ttk.Combobox(timKiem_frame, values= value_timkiem, font=("Arial", 10))
    cb_timkiem.grid(row=0, column=1, padx=5, pady=10)
    text_timkiem = Entry(timKiem_frame)
    text_timkiem.grid(row=0, column=2, padx=5, pady=10)
    button_tk = Button(timKiem_frame, text="Tìm kiếm") #, command=btnTimKiem)
    button_tk.grid(row=0, column=3, padx=5, pady=10)
    button_xemtatca = Button(timKiem_frame, text="Xem tất cả") #, command=btnXemTatca)
    button_xemtatca.grid(row=0, column=4, padx=0, pady=10)

    table_frame = Frame(right_frame_qly)
    table_frame.pack(pady=20)

    tbscrolly = Scrollbar(table_frame)
    tbscrolly.pack(side=RIGHT, fill="y")
    tbscrollx = Scrollbar(table_frame, orient="horizontal")
    tbscrollx.pack(fill="x", side=BOTTOM)

    table = ttk.Treeview(table_frame, yscrollcommand=tbscrolly, xscrollcommand=tbscrollx, selectmode="extended", height=630) 
    table.pack()
    tbscrolly.config(command=table.yview)
    tbscrollx.config(command=table.xview)

    table['column'] = ("Mã nhân viên", "Họ tên", "Ngày sinh", "Số điện thoại", "Giới tính", "Chức vụ", "Email")
    table.column("#0", width=0, stretch=NO)
    table.column("Mã nhân viên", anchor=CENTER, width=80)
    table.column("Họ tên", anchor=W, width=100)
    table.column("Ngày sinh", anchor=CENTER, width=80)
    table.column("Số điện thoại", anchor=CENTER, width=80)
    table.column("Giới tính", anchor=CENTER, width=60)
    table.column("Chức vụ", anchor=CENTER, width=80)
    table.column("Email", anchor=CENTER, width=80)

    table.heading("#0", text="", anchor=CENTER)
    table.heading("Mã nhân viên", text="Mã nhân viên", anchor=CENTER)
    table.heading("Họ tên", text="Họ tên", anchor=W)
    table.heading("Ngày sinh", text="Ngày sinh", anchor=CENTER)
    table.heading("Số điện thoại", text="Số điện thoại", anchor=CENTER)
    table.heading("Giới tính", text="Giới tính", anchor=CENTER)
    table.heading("Chức vụ", text="Chức vụ", anchor=CENTER)
    table.heading("Email", text="Email", anchor=CENTER)

    '''table.tag_configure('oddrow', background="white")
    table.tag_configure('evenrow', background="lightblue")'''

    # center_frame
    info_frame = Frame(center_frame, background="white")
    info_frame.pack()
    lb_info = Label(info_frame, text="Thông tin nhân viên", font=("Helvetica", 25))
    lb_info.grid(row=0, column=0, padx=0, pady=20, columnspan=2)

    lb_manv = CTkLabel(info_frame, text="Mã nhân viên", font=("Helvetica", 16))
    lb_manv.grid(row=1, column=0, pady=10)
    text_manv = CTkEntry(info_frame, font=("Helvetica", 15), corner_radius=20, text_color="black", border_width=2)
    text_manv.grid(row=1, column=1, pady=10)

    lb_ten = CTkLabel(info_frame, text="Họ tên", font=("Helvetica", 16))
    lb_ten.grid(row=2, column=0, pady=10)
    text_ten = CTkEntry(info_frame, font=("Helvetica", 15), corner_radius=20, text_color="black", border_width=2)
    text_ten.grid(row=2, column=1, pady=10)

    lb_ngaysinh = CTkLabel(info_frame, text="Ngày sinh", font=("Helvetica", 16))
    lb_ngaysinh.grid(row=3, column=0, pady=10)
    text_ngaysinh = CTkEntry(info_frame, font=("Helvetica", 15), corner_radius=20, text_color="black", border_width=2)
    text_ngaysinh.grid(row=3, column=1, pady=10)

    lb_sdt = CTkLabel(info_frame, text="Số điện thoại", font=("Helvetica", 16))
    lb_sdt.grid(row=4, column=0, pady=10)
    text_sdt = CTkEntry(info_frame, font=("Helvetica", 15), corner_radius=20, text_color="black", border_width=2)
    text_sdt.grid(row=4, column=1, pady=10)

    lb_gioitinh = CTkLabel(info_frame, text="Giới tính", font=("Helvetica", 16))
    lb_gioitinh.grid(row=5, column=0, pady=10)
    values_gioitinh = ["Nam", "Nữ"]
    cb_gioitinh = ttk.Combobox(info_frame, values=values_gioitinh, font=("Helvetica", 10), width=15)
    cb_gioitinh.grid(row=5, column=1, pady=10)

    lb_chucvu = CTkLabel(info_frame, text="Chức vụ", font=("Helvetica", 16))
    lb_chucvu.grid(row=6, column=0, pady=10)
    values_chucvu = ["Quản lý", "Nhân viên", "Thực tập"]
    cb_chucvu = ttk.Combobox(info_frame, values=values_chucvu, font=("Helvetica", 10), width=15)
    cb_chucvu.grid(row=6, column=1, pady=10)

    lb_email = CTkLabel(info_frame, text="Email", font=("Helvetica", 16))
    lb_email.grid(row=7, column=0, pady=5)
    text_email = CTkEntry(info_frame, font=("Helvetica", 15), corner_radius=20, text_color="black", border_width=2)
    text_email.grid(row=7, column=1, pady=5)
    
    button_capnhat = CTkButton(info_frame, text="Cập Nhật", corner_radius=30, border_width=2,
                               border_color="#87CEFA", text_color="white", hover_color="#00BFFF", font=("Helvetica", 15)) #, command=btnCapNhat
    button_capnhat.grid(row=8, column=1)
    button_xoa = CTkButton(info_frame, text="Xoá", corner_radius=30, border_width=2,
                           border_color="#87CEFA", text_color="white", hover_color="#00BFFF", font=("Helvetica", 15)) #, command=btnXoa
    button_xoa.grid(row=8, column=0, padx=10, pady=30)

    button_lammoi = CTkButton(info_frame, text="Làm mới", corner_radius=30, border_width=2,
                               border_color="#87CEFA", text_color="white", hover_color="#00BFFF", font=("Helvetica", 15)) #, command=btnLamMoi
    button_lammoi.grid(row=9, column=0)
    button_xemanh = CTkButton(info_frame, text="Xem ảnh", corner_radius=30, border_width=2,
                              border_color="#87CEFA", text_color="white", hover_color="#00BFFF", font=("Helvetica", 15)) #, command=btnXemAnh)
    button_xemanh.grid(row=9, column=1)



   
    
