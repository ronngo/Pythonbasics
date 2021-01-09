from Model import Person

def startView():
    print('Xây dựng MVC')
    key = input('Bạn có muốn xem tất cả dữ liệu không? [y/n] ')
    return key

def endView():
    print('See You')

def showAllView(danhsach):
    for person in danhsach:
        print(person.name, ',', person.address, ',', person.price)
    print('Tổng cộng có ', len(danhsach), 'dòng xe hơi')