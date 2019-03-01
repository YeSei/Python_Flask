__author__ = "Deng Yangjie"
'''
@ID:SA18225058
@copyright:USTC
@time:''
this module is for:
'''
from flask import render_template, flash, redirect, url_for, request
from forms import Store_Flights, Store_Hotels, Store_Cars, Store_Customers, LoginForm, RegistrationForm, Update_Flights_left,\
    Update_Flights_right, Res_Flights_right, Update_Hotels_left, Update_Hotels_right, Update_Cars_left, Update_Cars_right,\
    Res_Hotels_right, Res_cars_right, User_Travel
from models import Flights, Hotels, Cars, Reservations, User, Res_Flights, Res_Hotels,Res_Cars

from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user, login_required
from init import app, db



@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='旅游预定系统')

@app.route('/store')
def store():
    return render_template('store.html', title='旅游预定系统-入库选择')

@app.route('/store_flight', methods=['GET', 'POST'])
def store_flight():
    flights = Store_Flights()
    if flights.validate_on_submit():
        flight = Flights(flightnum=flights.flightnum.data, price=flights.price.data, numseats=flights.numseats.data,
                         numavail=flights.numavail.data, fromcity=flights.fromcity.data, arivcity=flights.arivcity.data)
        db.session.add(flight)
        db.session.commit()
        flash('Congratulations!')
        return render_template('end.html', title='旅游预定系统')
    return render_template('store_flight.html', title='旅游预定系统-航班入库', form=flights)


@app.route('/store_hotel', methods=['GET', 'POST'])
def store_hotel():
    hotels = Store_Hotels()
    if hotels.validate_on_submit():
        hotel = Hotels(location=hotels.location.data, price=hotels.price.data, numrooms=hotels.numrooms.data,
                         numavail=hotels.numavail.data, )
        db.session.add(hotel)
        db.session.commit()
        flash('Congratulations!')
        return render_template('end.html', title='旅游预定系统')
    return render_template('store_hotel.html', title='旅游预定系统-酒店入库', form=hotels)


@app.route('/store_car', methods=['GET', 'POST'])
def store_car():
    cars = Store_Cars()
    if cars.validate_on_submit():
        car = Cars(location=cars.location.data, price=cars.price.data, numcars=cars.numcars.data,
                         numavail=cars.numavail.data, )
        db.session.add(car)
        db.session.commit()
        flash('Congratulations!')
        return render_template('end.html', title='旅游预定系统')
    return render_template('store_car.html', title='旅游预定系统-出租车入库', form=cars)


@app.route('/store_customer', methods=['GET', 'POST'])
def store_customer():
    customers = Store_Customers()
    if customers.validate_on_submit():
        customer = Customers(custname=customers.location.data,)
        db.session.add(customer)
        db.session.commit()
        flash('Congratulations!')
        return render_template('end.html', title='旅游预定系统')
    return render_template('store_customer.html', title='旅游预定系统-客户入库', form=customers)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/update')
def update():
    return render_template('update.html', title='旅游预定系统-更新选择')


@app.route('/update_flight', methods=['GET', 'POST'])
def update_flight():
    form = Update_Flights_left()
    if form.validate_on_submit():
        flight = Flights.query.filter_by(flightnum=int(form.flightnum.data)).first_or_404()
        return render_template('update_flight.html', title='旅游预定系统-航班更新', form=form, flight1=flight)
    return render_template('update_flight.html', title='旅游预定系统-航班更新', form=form)


@app.route('/update_flight_right', methods=['GET', 'POST'])
def update_flight_right():
    form = Update_Flights_right()
    if form.validate_on_submit():
        flight = Flights.query.filter_by(flightnum=int(form.flightnum1.data)).first_or_404()
        flight.flightnum = form.flightnum2.data
        flight.price = form.price.data
        flight.numseats = form.numseats.data
        flight.numavail = form.numavail.data
        flight.fromcity = form.fromcity.data
        flight.arivcity = form.arivcity.data
        db.session.commit()
        flash('Congratulations!')
        return redirect(url_for('index'))
    return render_template('update_flight_right.html', title='旅游预定系统-航班更新', form=form)


@app.route('/update_hotel', methods=['GET', 'POST'])
def update_hotel():
    form = Update_Hotels_left()
    if form.validate_on_submit():
        hotel = Hotels.query.filter_by(hotels_id=int(form.hotels_id.data)).first_or_404()
        return render_template('update_hotel.html', title='旅游预定系统-酒店更新', form=form, hotel=hotel)
    return render_template('update_hotel.html', title='旅游预定系统-酒店更新', form=form)


@app.route('/update_hotel_right', methods=['GET', 'POST'])
def update_hotel_right():
    form = Update_Hotels_right()
    if form.validate_on_submit():
        hotel = Hotels.query.filter_by(hotels_id=int(form.hotels_id1.data)).first_or_404()
        hotel.hotels_id = form.hotels_id2.data
        hotel.location = form.location.data
        hotel.price = form.price.data
        hotel.numrooms = form.numrooms.data
        hotel.numavail = form.numavail.data
        db.session.commit()
        flash('Congratulations!')
        return redirect(url_for('index'))
    return render_template('update_hotel_right.html', title='旅游预定系统-酒店更新', form=form)


@app.route('/update_car', methods=['GET', 'POST'])
def update_car():
    form = Update_Cars_left()
    if form.validate_on_submit():
        car = Cars.query.filter_by(cars_id=int(form.cars_id.data)).first_or_404()
        return render_template('update_car.html', title='旅游预定系统-出租车更新', form=form, hotel=car)
    return render_template('update_car.html', title='旅游预定系统-出租车更新', form=form)


@app.route('/update_car_right', methods=['GET', 'POST'])
def update_car_right():
    form = Update_Cars_right()
    if form.validate_on_submit():
        car = Cars.query.filter_by(cars_id=int(form.cars_id1.data)).first_or_404()
        car.cars_id = form.cars_id2.data
        car.location = form.location.data
        car.price = form.price.data
        car.numcars = form.numcars.data
        car.numavail = form.numavail.data
        db.session.commit()
        flash('Congratulations!')
        return redirect(url_for('index'))
    return render_template('update_car_right.html', title='旅游预定系统-出租车更新', form=form)


@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    return render_template('reservation.html', title='旅游预定系统-订单选择')


@app.route('/res_flight', methods=['GET', 'POST'])
def res_flight():
    form = Update_Flights_left()
    if form.validate_on_submit():
        flight = Flights.query.filter_by(flightnum=int(form.flightnum.data)).first_or_404()
        return render_template('res_flight.html', title='旅游预定系统-航班查询', form=form, flight1=flight)
    return render_template('res_flight.html', title='旅游预定系统-航班查询',form=form)


@app.route('/res_flight_right', methods=['GET', 'POST'])
def res_flight_right():
    form = Res_Flights_right()
    if form.validate_on_submit():
        res = Reservations(username=form.username.data, resvtype=0, user_id=current_user.id, )
        db.session.add(res)
        db.session.commit()
        res_f = Res_Flights(reskey=res.resvkey, flightnum=form.flightnum.data)
        db.session.add(res_f)
        flight = Flights.query.filter_by(flightnum=int(form.flightnum.data)).first_or_404()
        flight.numavail = flight.numavail - 1
        db.session.commit()
        flash('Congratulations!')
        return render_template('end.html', title='旅游预定系统')
    return render_template('res_flight_right.html', title='旅游预定系统-提交订单', form=form)


@app.route('/res_hotel', methods=['GET', 'POST'])
def res_hotel():
    form = Update_Hotels_left()
    if form.validate_on_submit():
        hotel = Hotels.query.filter_by(hotels_id=int(form.hotels_id.data)).first_or_404()
        return render_template('res_hotel.html', title='旅游预定系统-酒店查询', form=form, hotel=hotel)
    return render_template('res_hotel.html', title='旅游预定系统-酒店查询',form=form)


@app.route('/res_hotel_right', methods=['GET', 'POST'])
def res_hotel_right():
    form = Res_Hotels_right()
    if form.validate_on_submit():
        res = Reservations(username=form.username.data, resvtype=1, user_id=current_user.id, )
        db.session.add(res)
        db.session.commit()
        res_f = Res_Hotels(reskey=res.resvkey, hotels_id=form.hotels_id.data)
        hotel = Hotels.query.filter_by(hotels_id=int(form.hotels_id.data)).first_or_404()
        hotel.numavail = hotel.numavail - 1
        db.session.add(res_f)
        db.session.commit()
        flash('Congratulations!')
        return render_template('end.html', title='旅游预定系统')
    return render_template('res_hotel_right.html', title='旅游预定系统-提交订单', form=form)

@app.route('/res_car', methods=['GET', 'POST'])
def res_car():
    form = Update_Cars_left()
    if form.validate_on_submit():
        car = Cars.query.filter_by(cars_id=int(form.cars_id.data)).first_or_404()
        return render_template('res_car.html', title='旅游预定系统-出租车查询', form=form, car=car)
    return render_template('res_car.html', title='旅游预定系统-出租车查询',form=form)


@app.route('/res_car_right', methods=['GET', 'POST'])
def res_car_right():
    form = Res_cars_right()
    if form.validate_on_submit():
        res = Reservations(username=form.username.data, resvtype=2, user_id=current_user.id, )
        db.session.add(res)
        db.session.commit()
        res_f = Res_Cars(reskey=res.resvkey, cars_id=form.cars_id.data)
        car = Cars.query.filter_by(cars_id=int(form.cars_id.data)).first_or_404()
        car.numavail = car.numavail - 1
        db.session.add(res_f)
        db.session.commit()
        flash('Congratulations!')
        return render_template('end.html', title='旅游预定系统')
    return render_template('res_car_right.html', title='旅游预定系统-提交订单', form=form)


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html', title='旅游预定系统-查询')


@app.route('/search_flight', methods=['GET', 'POST'])
def search_flight():
    form = Update_Flights_left()
    if form.validate_on_submit():
        flight = Flights.query.filter_by(flightnum=int(form.flightnum.data)).first_or_404()
        return render_template('search_flight.html', title='旅游预定系统-航班查询', form=form, flight1=flight)
    return render_template('search_flight.html', title='旅游预定系统-航班查询', form=form)

@app.route('/search_hotel', methods=['GET', 'POST'])
def search_hotel():
    form = Update_Hotels_left()
    if form.validate_on_submit():
        hotel = Hotels.query.filter_by(hotels_id=int(form.hotels_id.data)).first_or_404()
        return render_template('search_hotel.html', title='旅游预定系统-酒店查询', form=form, hotel=hotel)
    return render_template('search_hotel.html', title='旅游预定系统-酒店查询',form=form)


@app.route('/search_car', methods=['GET', 'POST'])
def search_car():
    form = Update_Cars_left()
    if form.validate_on_submit():
        car = Cars.query.filter_by(cars_id=int(form.cars_id.data)).first_or_404()
        return render_template('search_car.html', title='旅游预定系统-出租车查询', form=form, car=car)
    return render_template('search_car.html', title='旅游预定系统-出租车查询',form=form)


@app.route('/search_user', methods=['GET', 'POST'])
def search_user():
    form = User_Travel()
    if form.validate_on_submit():
        user_id = int(form.user_id.data)
        resvs = Reservations.query.filter_by(user_id=int(form.user_id.data)).all()
        res_f = []
        res_h = []
        res_c = []
        for res in resvs:
            if res.resvtype == 0:
                r_flight = Res_Flights.query.filter_by(reskey=res.resvkey).first()
                res_f.append(r_flight)
            elif res.resvtype == 1:
                r_hotel = Res_Hotels.query.filter_by(reskey=res.resvkey).first()
                res_h.append(r_hotel)
            elif res.resvtype == 2:
                r_car = Res_Cars.query.filter_by(reskey=res.resvkey).first()
                res_c.append(r_car)
        return render_template('search_user.html', title='旅游预定系统-旅程查询', form=form, resvs=user_id, res_f=res_f,res_h=res_h,res_c=res_c)
    return render_template('search_user.html', title='旅游预定系统-旅程查询',form=form)