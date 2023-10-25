def load_nav():
    return [
        {
            "id": 1,
            "name":"Trang phụ"
        },
        {
            "id": 2,
            "name": "Liên hệ"
        }
    ]

def load_categories(kw):
    products = [
        {
            "id" : 1,
            "name":"Sách",
            "price": 20000,
            "image": "https://img5.thuthuatphanmem.vn/uploads/2022/01/12/anh-che-tokuda-hai-huoc_101658516.jpg"
        },
        {
            "id": 2,
            "name": "Sói Cừu",
            "price": 20000,
            "image": "https://img5.thuthuatphanmem.vn/uploads/2022/01/12/anh-che-tokuda-hai-huoc_101658516.jpg"
        },
        {
            "id": 3,
            "name": "Kẻ điên",
            "price": 20000,
            "image": "https://img5.thuthuatphanmem.vn/uploads/2022/01/12/anh-che-tokuda-hai-huoc_101658516.jpg"
        },
        {
            "id": 4,
            "name": "Sách",
            "price": 20000,
            "image": "https://img5.thuthuatphanmem.vn/uploads/2022/01/12/anh-che-tokuda-hai-huoc_101658516.jpg"
        },
        {
            "id": 5,
            "name": "Sách",
            "price": 20000,
            "image": "https://th.bing.com/th/id/OIP.sG3uELc_wRRSpvGfwsvnPQHaHa?pid=ImgDet&rs=1"
        },
        {
            "id": 6,
            "name": "Sách",
            "price": 20000,
            "image": "https://down-vn.img.susercontent.com/file/d40c6036724a015fa3432a6fea1dbbd1"
        },
        {
            "id": 7,
            "name": "Sách",
            "price": 20000,
            "image": "https://down-vn.img.susercontent.com/file/d40c6036724a015fa3432a6fea1dbbd1"
        },
        {
            "id": 8,
            "name": "Sách",
            "price": 20000,
            "image": "https://down-vn.img.susercontent.com/file/d40c6036724a015fa3432a6fea1dbbd1"
        },

    ]

    if kw:
        products = [ p for p in products if p["name"].find(kw)>=0]

    return products