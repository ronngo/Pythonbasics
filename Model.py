class Person:
    # Thuộc tính có thể khơi tạo mặc định hoặc để trống
    nationality = "Car"

    # Phương thức khởi tạo
    def __init__(self, name,address , price):
        # Khởi tạo thuộc tính của lớp ngay trong hàm init
        self.name = name
        self.address = address
        self.price = price

        # Thiết lập giá trị cho thuộc tính
    def set_nationality(self, nationality):
        self.nationality = nationality

    # Lấy thông tin của đối tượng
    def __str__(self):
        return "{} có tuổi là {} và quốc tịch là {}".format(self.name, self.price, self.address, self.nationality)

    @classmethod
    #Phương thức giả định lấy dữ liệu
    def get_All_Person(self):
        database = [("Toyota Vios", "hue", 12), ("Hyundai Grand i10", "Hue", 12), ("Hyundai Accent", "Hue", 16)]
        result = []  #Trả về kết quả là list gồm các đối tượng Person
        #Chuyển database ở trên thành các đối tượng Person - tương tự việc lấy trong CSDL sau này
        for idx, (name, address, price) in enumerate(database):
            tam = Person(name, address, price)
            result.append(tam)
        return result