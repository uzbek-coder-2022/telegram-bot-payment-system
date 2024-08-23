from aiogram.types import Message, ContentType
from aiogram.filters import Command
from aiogram import Router
from aiogram.types import LabeledPrice, PreCheckoutQuery
from aiogram import F
from loader import bot
from data.config import PAYMENT_TOKEN

payment_router = Router()


# Buy - bu kommanda botda mahsulot sotib olish uchun yoziladi
@payment_router.message(Command("buy"))
async def cmd_buy(message: Message):
    await bot.send_invoice(
        chat_id=message.chat.id,  # Foydalanuvchi yoki chat ID si
        title="Olma",  # Mahsulot nomi
        description="Intensiv bog'da o'stirilgan shirin va suvli olma",  # Mahsulot haqida batafsil ma'lumot
        payload="123",  # Unikal to'lov identifikatori (odatda mahsulot ID si)
        provider_token=PAYMENT_TOKEN,  # To'lov provayderi tokeni
        currency="UZS",  # Valyuta kodi (ISO 4217 formatida)
        prices=[
            LabeledPrice(label="Mahsulot narxi", amount=1000000),  # 10,000 so'm (1 tiyin = 1/100 so'm)
            LabeledPrice(label="Chegirma", amount=-100000),  # -1,000 so'm chegirma
        ],  # Mahsulot narxi va boshqa qiymatlar (masalan, QQS, chegirma)
        # max_tip_amount=200000,  # Taklif etiladigan maksimal choychaqa miqdori (2000 so'm)
        # suggested_tip_amounts=[100, 50000, 100000, 150000],  # Foydalanuvchiga ko'rsatiladigan choychaqa variantlari (500 so'm, 1000 so'm, 1500 so'm)
        start_parameter="test-invoice-payload",  # Foydalanuvchini invoiceda belgilangan to'lovga yo'naltiruvchi maxsus parameter
        provider_data=None,  # To'lov provayderiga maxsus ma'lumotlarni yuborish uchun (odatda kerak emas)
        photo_url="https://images.everydayhealth.com/images/diet-nutrition/apples-101-about-1440x810.jpg?sfvrsn=f86f2644_5",  # Mahsulot rasmi URL manzili
        photo_size=600,  # Rasm hajmi (baytlarda)
        photo_width=800,  # Rasm eni (piksellarda)
        photo_height=450,  # Rasm balandligi (piksellarda)
        need_name=False,  # Foydalanuvchi ismini talab qilish
        need_phone_number=False,  # Foydalanuvchi telefon raqamini talab qilish
        need_email=False,  # Foydalanuvchi elektron pochta manzilini talab qilish
        need_shipping_address=False,  # Yetkazib berish manzilini talab qilish
        send_phone_number_to_provider=False,  # Foydalanuvchi telefon raqamini to'lov provayderiga yuborish
        send_email_to_provider=False,  # Foydalanuvchi elektron pochta manzilini to'lov provayderiga yuborish
        is_flexible=False,  # To'lov miqdori o'zgaruvchanmi yoki yo'qligini belgilash (True bo'lsa, miqdor o'zgarishi mumkin)
        disable_notification=False,  # Xabarning foydalanuvchiga xabar berilmasdan yuborilishi (True bo'lsa, xabarsiz yuboriladi)
        protect_content=True,  # Xabarni boshqa foydalanuvchilar bilan ulashishni cheklash (True bo'lsa, kontent himoyalanadi)
        reply_to_message_id=None,  # Xabarni qaysi xabarga javob sifatida yuborilishini belgilash
        allow_sending_without_reply=False,  # Javob xabarsiz yuborilishini ruxsat etish (True bo'lsa, javob xabarsiz yuboriladi)
        reply_markup=None,  # Foydalanuvchi interfeysi elementlarini belgilash (tugmalar va boshqalar)
        request_timeout=10  # To'lov amalga oshirilishidan oldin beriladigan vaqti
    )


# Pre-Checkout Query handler - foydalanuvchi to'lovni tasdiqlashdan oldin bu handler ishlaydi
@payment_router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    # Pre-Checkout Query-ni tasdiqlash. Bu foydalanuvchi to'lovni amalga oshirishi mumkinligini bildiradi.
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


# Successful Payment handler - foydalanuvchi to'lovni muvaffaqiyatli amalga oshirganda bu handler ishlaydi
@payment_router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: Message):
    print("Muvaffaqiyatli to'lov:")

    # message.successful_payment orqali to'lov haqidagi barcha ma'lumotlarni olish va ularni dictionary sifatida chiqarish
    payment_info = message.successful_payment.to_python()

    # To'lov haqidagi barcha ma'lumotlarni chop etish
    for k, v in payment_info.items():
        print(f"{k} = {v}")

    # Foydalanuvchiga to'lov muvaffaqiyatli amalga oshirilgani haqida xabar yuborish
    await bot.send_message(
        message.chat.id,
        f"To'lov muvaffaqiyatli amalga oshirildi! Jami summa: {message.successful_payment.total_amount // 100} {message.successful_payment.currency}."
    )
