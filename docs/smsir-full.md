# راهنمای استفاده از API سایت sms.ir

> **این یک پروژه‌ی مستقل و غیررسمی است.** نویسنده وابسته به sms.ir نیست؛ محتوا از راهنمای پنل sms.ir استخراج، بازنویسی و سلسله‌مراتبی شده تا استفاده از آن — از جمله در ابزارهای هوش مصنوعی — ساده‌تر باشد. برای مرجع رسمی همیشه به [پنل و مستندات خود sms.ir](https://sms.ir) نیز مراجعه کنید.

## فهرست مطالب

- [1. مقدمه](#1-مقدمه)
  - [1.1. HTTP REQUEST HEADER](#11-http-request-header)
  - [1.2. HTTP STATUS CODE](#12-http-status-code)
  - [1.3. UNIX Time](#13-unix-time)
  - [1.4. مدل بازگشتی](#14-مدل-بازگشتی)
    - [1.4.1. Response Body](#141-response-body)
  - [1.5. AUTHORIZATION – احراز هویت](#15-authorization--احراز-هویت)
- [2. Sandbox](#2-sandbox)
  - [2.1. ویژگی‌های محیط Sandbox](#21-ویژگیهای-محیط-sandbox)
    - [2.1.1. کلید API مخصوص Sandbox](#211-کلید-api-مخصوص-sandbox)
    - [2.1.2. داده‌های شبیه‌سازی‌شده](#212-دادههای-شبیهسازیشده)
    - [2.1.3. قالب پیش‌فرض متد Verify در محیط Sandbox](#213-قالب-پیشفرض-متد-verify-در-محیط-sandbox)
    - [2.1.4. عدم ثبت گزارشات](#214-عدم-ثبت-گزارشات)
  - [2.2. نکات کلیدی](#22-نکات-کلیدی)
  - [2.3. نحوه استفاده از محیط Sandbox](#23-نحوه-استفاده-از-محیط-sandbox)
    - [2.3.1. ایجاد کلید Sandbox](#231-ایجاد-کلید-sandbox)
    - [2.3.2. ارسال درخواست](#232-ارسال-درخواست)
  - [2.4. نمونه درخواست ارسال Verify](#24-نمونه-درخواست-ارسال-verify)
    - [2.4.1. بررسی پاسخ‌ها](#241-بررسی-پاسخها)
- [3. ارسال‌ها](#3-ارسالها)
  - [3.1. ارسال گروهی](#31-ارسال-گروهی)
    - [3.1.1. پارامترهای بدنه درخواست](#311-پارامترهای-بدنه-درخواست)
    - [3.1.2. مدل دیتای بازگشتی](#312-مدل-دیتای-بازگشتی)
    - [3.1.3. نمونه کد](#313-نمونه-کد)
  - [3.2. ارسال نظیر به نظیر](#32-ارسال-نظیر-به-نظیر)
    - [3.2.1. پارامترهای بدنه درخواست](#321-پارامترهای-بدنه-درخواست)
    - [3.2.2. مدل دیتای بازگشتی](#322-مدل-دیتای-بازگشتی)
    - [3.2.3. نمونه کد](#323-نمونه-کد)
  - [3.3. حذف ارسال زمان‌بندی شده](#33-حذف-ارسال-زمانبندی-شده)
    - [3.3.1. پارامترهای درخواست](#331-پارامترهای-درخواست)
    - [3.3.2. مدل دیتای بازگشتی](#332-مدل-دیتای-بازگشتی)
    - [3.3.3. نمونه کد](#333-نمونه-کد)
  - [3.4. ارسال Verify](#34-ارسال-verify)
    - [3.4.1. پارامترهای بدنه درخواست](#341-پارامترهای-بدنه-درخواست)
    - [3.4.2. مدل دیتای بازگشتی](#342-مدل-دیتای-بازگشتی)
    - [3.4.3. نمونه کد](#343-نمونه-کد)
  - [3.5. ارسال از طریق URL](#35-ارسال-از-طریق-url)
    - [3.5.1. پارامترهای بدنه درخواست](#351-پارامترهای-بدنه-درخواست)
    - [3.5.2. مدل دیتای بازگشتی](#352-مدل-دیتای-بازگشتی)
    - [3.5.3. نمونه کد](#353-نمونه-کد)
- [4. گزارش‌ها](#4-گزارشها)
  - [4.1. گزارش پیامک (دریافت وضعیت)](#41-گزارش-پیامک-دریافت-وضعیت)
    - [4.1.1. مدل دیتای بازگشتی](#411-مدل-دیتای-بازگشتی)
    - [4.1.2. نمونه کد](#412-نمونه-کد)
  - [4.2. گزارش مجموعه ارسال‌های روز](#42-گزارش-مجموعه-ارسالهای-روز)
    - [4.2.1. پارامترهای درخواست](#421-پارامترهای-درخواست)
    - [4.2.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)](#422-مدل-دیتای-بازگشتی-آرایهای-از-مدل-زیر)
    - [4.2.3. نمونه کد](#423-نمونه-کد)
  - [4.3. گزارش مجموعه ارسال](#43-گزارش-مجموعه-ارسال)
    - [4.3.1. پارامترهای درخواست](#431-پارامترهای-درخواست)
    - [4.3.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)](#432-مدل-دیتای-بازگشتی-آرایهای-از-مدل-زیر)
    - [4.3.3. نمونه کد](#433-نمونه-کد)
  - [4.4. گزارش ارسال‌های روز](#44-گزارش-ارسالهای-روز)
    - [4.4.1. پارامترهای درخواست](#441-پارامترهای-درخواست)
    - [4.4.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)](#442-مدل-دیتای-بازگشتی-آرایهای-از-مدل-زیر)
    - [4.4.3. نمونه کد](#443-نمونه-کد)
  - [4.5. گزارش ارسال‌های آرشیو شده](#45-گزارش-ارسالهای-آرشیو-شده)
    - [4.5.1. پارامترهای درخواست](#451-پارامترهای-درخواست)
    - [4.5.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)](#452-مدل-دیتای-بازگشتی-آرایهای-از-مدل-زیر)
    - [4.5.3. نمونه کد](#453-نمونه-کد)
  - [4.6. گزارش تازه‌ترین پیامک‌های دریافتی](#46-گزارش-تازهترین-پیامکهای-دریافتی)
    - [4.6.1. پارامترهای درخواست](#461-پارامترهای-درخواست)
    - [4.6.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)](#462-مدل-دیتای-بازگشتی-آرایهای-از-مدل-زیر)
    - [4.6.3. نمونه کد](#463-نمونه-کد)
  - [4.7. گزارش پیامک‌های دریافتی روز](#47-گزارش-پیامکهای-دریافتی-روز)
    - [4.7.1. پارامترهای درخواست](#471-پارامترهای-درخواست)
    - [4.7.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)](#472-مدل-دیتای-بازگشتی-آرایهای-از-مدل-زیر)
    - [4.7.3. نمونه کد](#473-نمونه-کد)
  - [4.8. گزارش پیامک‌های دریافتی آرشیو شده](#48-گزارش-پیامکهای-دریافتی-آرشیو-شده)
    - [4.8.1. پارامترهای درخواست](#481-پارامترهای-درخواست)
    - [4.8.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)](#482-مدل-دیتای-بازگشتی-آرایهای-از-مدل-زیر)
    - [4.8.3. نمونه کد](#483-نمونه-کد)
- [5. تنظیمات](#5-تنظیمات)
  - [5.1. دریافت مقدار اعتبار فعلی](#51-دریافت-مقدار-اعتبار-فعلی)
    - [5.1.1. دیتای بازگشتی](#511-دیتای-بازگشتی)
    - [5.1.2. نمونه کد](#512-نمونه-کد)
  - [5.2. دریافت لیست خطوط](#52-دریافت-لیست-خطوط)
    - [5.2.1. دیتای بازگشتی (آرایه‌ای از Long)](#521-دیتای-بازگشتی-آرایهای-از-long)
    - [5.2.2. نمونه کد](#522-نمونه-کد)
- [6. جداول کدهای وضعیت](#6-جداول-کدهای-وضعیت)
  - [6.1. کدهای وضعیت‌](#61-کدهای-وضعیت)
  - [6.2. کدهای وضعیت دلیوری](#62-کدهای-وضعیت-دلیوری)
- [7. کتابخانه‌های رسمی (SDK)](#7-کتابخانههای-رسمی-sdk)
  - [7.1. فهرست پکیج‌ها](#71-فهرست-پکیجها)
  - [7.2. شروع سریع به تفکیک زبان](#72-شروع-سریع-به-تفکیک-زبان)
  - [7.3. جدول تناظر متدهای API با متدهای هر SDK](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk)
  - [7.4. لایسنس و پشتیبانی](#74-لایسنس-و-پشتیبانی)

---

## 1. مقدمه

در این بخش مفاهیم و قراردادهای کلی مربوط به استفاده از وب سرویس sms.ir، شرح داده خواهند شد.

### 1.1. HTTP REQUEST HEADER

شما می‌توانید برای انجام تنظیمات ضروری و یا شخصی سازی شده، از هدرهای مشخص شده در جدول زیر استفاده نمایید.

| کلید      | مقدار                               | عملکرد                           |
| --------- | ----------------------------------- | -------------------------------- |
| ACCEPT    | application/json یا application/xml | دریافت خروجی با فرمت Json یا Xml |
| X-API-KEY | کلید تعریف شده در پنل               | احراز هویت                       |

### 1.2. HTTP STATUS CODE

تمامی درخواست‌های ارسالی دارای HTTP status code‌های بازگشتی مطابق جدول زیر می‌باشند.

| کد وضعیت | توضیح                         |
| -------- | ----------------------------- |
| 200      | عملیات موفقیت آمیز            |
| 400      | وقوع خطای منطقی               |
| 401      | وجود خطا در فرآیند احراز هویت |
| 429      | تعداد درخواست غیر مجاز        |
| 500      | خطای غیر منتظره               |

### 1.3. UNIX Time

واحد مقادیر مربوط به زمان در سطح این سامانه به صورت Unix Time و بر حسب ساعت هماهنگ جهانی (UTC) لحاظ شده است.

### 1.4. مدل بازگشتی

تمامی درخواست‌های ارسالی دارای مدل بازگشتی یکپارچه با ساختار زیر می‌باشند.

#### 1.4.1. Response Body

```JSON
{
    "status":1,
    "message":"موفق",
    "data":[
     30004505000027,
     10002166593818
    ]
}
```

| مشخصه   | توضیح                 |
| ------- | --------------------- |
| Status  | کد وضعیت              |
| Message | توضیحات وضعیت درخواست |
| Data    | دیتای بازگشتی         |

### 1.5. AUTHORIZATION – احراز هویت

به منظور هویت‌سنجی در هنگام استفاده از وب سرویس‌های SMS.ir ملزم به ارسال کلید خصوصی در بخش هدر درخواست مورد نظر می‌باشید. کلیدهای خصوصی شما در پنل برنامه‌نویسان قابل مشاهده و مدیریت می‌باشند. در هنگام فراخوانی متدهای سامانه کلید خصوصی را با عنوان X-API-KEY در هدر درخواست قرار دهید.

**X-API-KEY:** PN1TVeBeaAehFLJAKU4XdfpsFXsQguYfleO0bV4ceh6diTZid2hRXza3uSkBbDef

---

## 2. Sandbox

**Sandbox** محیطی تستی برای کاربران و توسعه‌دهندگان است که امکان آزمایش عملکرد درخواست‌ها را پیش از استفاده در محیط اصلی (Production) فراهم می‌کند. این محیط با داده‌های شبیه‌سازی‌شده به کاربران کمک می‌کند تا بدون ارسال پیامک واقعی یا کسر اعتبار، درخواست‌های خود را بررسی و بهینه کنند.

---

### 2.1. ویژگی‌های محیط Sandbox

#### 2.1.1. کلید API مخصوص Sandbox

برای استفاده از Sandbox باید از API Key مخصوص این محیط استفاده شود.

ساختار URLها، ورودی‌ها و خروجی‌ها مشابه محیط اصلی است.

**کلید Sandbox از مسیر زیر قابل ایجاد است:** برنامه‌نویسان ← لیست کلیدهای API ← ایجاد کلید جدید

#### 2.1.2. داده‌های شبیه‌سازی‌شده

پاسخ‌های بازگشتی شبیه‌سازی‌شده و فاقد اعتبار واقعی هستند.

خطاهای بازگشتی مشابه محیط اصلی هستند و صحت ورودی‌ها را بررسی می‌کنند.

#### 2.1.3. قالب پیش‌فرض متد Verify در محیط Sandbox

در محیط Sandbox، فقط یک قالب پیش‌فرض برای متد Verify فعال است:

**شناسه قالب:** `123456`

**متن قالب:** کد تایید شما `#CODE#`

این قالب پیش‌فرض به کاربران این امکان را می‌دهد که در شرایطی مانند عدم راه‌اندازی کامل سایت، نبود اینماد، یا توسعه محیط آزمایشی، کدهای خود را با استفاده از کلید وب سرویس نوع Sandbox در محیط تست بررسی و آزمایش کنند.

#### 2.1.4. عدم ثبت گزارشات

اطلاعات بازگشتی تنها در پاسخ به درخواست‌ها نمایش داده می‌شود و گزارشی در سامانه ثبت نمی‌شود.

---

### 2.2. نکات کلیدی

**کلید مخصوص Sandbox:** ارسال‌ها در این محیط به‌صورت شبیه‌سازی‌شده انجام می‌شوند، بدون اینکه پیامکی واقعی ارسال شود یا هزینه‌ای کسر گردد.

**عدم ثبت گزارشات:** گزارشی از ارسال‌ها در سامانه ثبت نمی‌شود و فقط پاسخ‌ها در همان لحظه نمایش داده می‌شوند.

**تطابق با محیط اصلی:** ورودی‌ها، خروجی‌ها و پیام‌های خطا مشابه محیط اصلی هستند.

**داده‌های شبیه‌سازی‌شده:** تمامی داده‌های بازگشتی صرفاً برای شبیه‌سازی عملکرد API ارائه می‌شوند و اعتبار واقعی ندارند.

---

### 2.3. نحوه استفاده از محیط Sandbox

#### 2.3.1. ایجاد کلید Sandbox

به بخش **برنامه‌نویسان ← لیست کلیدهای API ← ایجاد کلید جدید (نوع: Sandbox)** مراجعه کنید.

کلید ایجادشده را در هدر درخواست‌ها وارد کنید.

#### 2.3.2. ارسال درخواست

درخواست‌ها را با همان ساختار و URLهای محیط اصلی ارسال کنید.

---

### 2.4. نمونه درخواست ارسال Verify

**URL:** <https://api.sms.ir/v1/send/verify>

**Request Method:** POST

**Header:**

```JSON
{
        'Content-Type': 'application/json',
        'Accept': 'text/plain',
        'x-api-key': 'YOUR_SANDBOX_API_KEY'
}
```

**Request Body:**

```JSON
{
    "mobile": "919xxxx904",
    "templateId": 123456,
    "parameters": [
      {
        "name": "Code",
        "value": "12345"
      }
    ]
}
```

#### 2.4.1. بررسی پاسخ‌ها

در صورت موفقیت:

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": {
        "messageId": 89545112,
        "cost": 1.0
    }
}
```

---

## 3. ارسال‌ها

### 3.1. ارسال گروهی

این متد برای ارسال یک متن پیامک به گروهی از شماره موبایل‌ها مورد استفاده قرار می‌گیرد. همچنین شما می‌توانید با مقداردهی به پارامتر زمان ارسال، از قابلیت ارسال پیامک زمان‌بندی شده نیز استفاده نمایید.

**URL:** <https://api.sms.ir/v1/send/bulk>

**Request Method:** POST

> این متد برای ارسال‌های ساده (تکی یا گروهی) از خط اختصاصی شما مناسب است. در صورتی که خط اختصاصی شما به‌عنوان خط خدماتی فعال نشده باشد، پیامک‌های ارسالی با این متد ممکن است برای مخاطبانی که پیامک‌های تبلیغاتی را مسدود کرده‌اند ارسال نشود (به لیست سیاه اصابت کند).

> حداکثر تعداد مجاز شماره‌های مقصد 100 می‌باشد.
> برای ارسال زمان‌بندی شده، انتخاب زمان گذشته نامعتبر می‌باشد.
> برای ارسال زمان‌بندی شده، زمان معتبر می‌تواند در بازه یک ساعت آینده تا حداکثر 365 روز آینده در نظر گرفته شود.

#### 3.1.1. پارامترهای بدنه درخواست

| مشخصه        | ارسال   | نوع             | توضیح                                                           |
| ------------ | ------- | --------------- | --------------------------------------------------------------- |
| lineNumber   | اجباری  | Long            | شماره خط ارسالی                                                 |
| MessageText  | اجباری  | String          | متن پیام کوتاه                                                  |
| Mobiles      | اجباری  | Array of String | شماره موبایل‌ها                                                  |
| SendDateTime | اختیاری | UnixTime        | زمان ارسال پیامک (در صورت خالی بودن، ارسال در لحظه انجام می‌شود) |

**Request Body:**

```JSON
{
    "lineNumber": 30004505000017,
    "messageText": "سرویس پیامکی ایده پردازان با بیش از یک دهه سابقه همراه شماست",
    "mobiles": [
        "0912xxxx677",
        "0919xxxx904"
    ]
}
```

#### 3.1.2. مدل دیتای بازگشتی

| مشخصه      | نوع              | توضیح                                |
| ---------- | ---------------- | ------------------------------------ |
| PackId     | Guid             | شناسه یکتای مجموعه ارسال             |
| MessageIds | Array of Integer | آرایه‌ای از شناسه‌های یکتای هر پیامک |
| Cost       | Decimal          | اعتبار مصرفی مجموعه ارسال            |

> در آرایه‌ی `MessageIds`، هر عضو می‌تواند مقدار id متناظر پیامک، `0` یا `null` باشد؛ مقدار `0` به معنای قرارگرفتن شماره در لیست سیاه است و مقدار `null` به معنای نامعتبر بودن شماره یا بیش از حد بودن طول متن برای آن مخاطب است.

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": {
        "packId": "2b99e63c-9bf8-4a21-9bfe-3f72dc1b46f1",
        "messageIds": [
            86522023,
            86522024
        ],
        "cost": 2.0
    }
}
```

#### 3.1.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var payload = @"{" + "\n" +
@"    ""lineNumber"": 300000000000," + "\n" +
@"    ""messageText"": ""Your Text""," + "\n" +
@"    ""mobiles"": [" + "\n" +
@"        ""Your Mobile 1""" + "\n" +
@"    ]," + "\n" +
@"    ""sendDateTime"": null" + "\n" +
@"}";
HttpContent content = new StringContent(payload, Encoding.UTF8, "application/json");
var response = await httpClient.PostAsync("https://api.sms.ir/v1/send/bulk", content);
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("X-API-KEY", "YOURAPIKEY");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "lineNumber": 300000000000,
  "messageText": "Your Text",
  "mobiles": [
    "Your Mobile 1",
    "Your Mobile 2"
  ],
  "sendDateTime": null
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/send/bulk", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var data = JSON.stringify({
  "lineNumber": 300000000000,
  "messageText": "Your Text",
  "mobiles": [
    "Your Mobile 1",
    "Your Mobile 2"
  ],
  "sendDateTime": null
});

var config = {
  method: 'post',
  url: 'https://api.sms.ir/v1/send/bulk',
  headers: {
    'X-API-KEY': 'YOURAPIKEY',
    'Content-Type': 'application/json'
  },
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
CURLOPT_URL => 'https://api.sms.ir/v1/send/bulk',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "lineNumber": 300000000000,
    "messageText": "Your Text",
    "mobiles": [
        "Your Mobile 1",
        "Your Mobile 2"
    ],
    "sendDateTime": null
}',
  CURLOPT_HTTPHEADER => array(
    'X-API-KEY: YOURAPIKEY',
    'Content-Type: application/json'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = json.dumps({
  "lineNumber": 300000000000,
  "messageText": "Your Text",
  "mobiles": [
    "Your Mobile 1",
    "Your Mobile 2"
  ],
  "sendDateTime": None
})
headers = {
  'X-API-KEY': 'YOURAPIKEY',
  'Content-Type': 'application/json'
}
conn.request("POST", "/v1/send/bulk", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
    .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\r\n    \"lineNumber\": 300000000000,\r\n    \"messageText\": \"Your Text\",\r\n
  \"mobiles\": [\r\n        \"Your Mobile 1\",\r\n        \"Your Mobile 2\"\r\n    ],\r\n    \"sendDateTime\": null\r\n}");
Request request = new Request.Builder()
    .url("https://api.sms.ir/v1/send/bulk")
    .method("POST", body)
    .addHeader("X-API-KEY", "YOURAPIKEY")
    .addHeader("Content-Type", "application/json")
    .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

### 3.2. ارسال نظیر به نظیر

این متد برای ارسال به گروهی از موبایل‌ها با متن‌های متفاوت برای هر کدام، مورد استفاده قرار می‌گیرد. همچنین شما می‌توانید با مقداردهی به پارامتر زمان ارسال، از قابلیت ارسال پیامک زمان‌بندی شده نیز استفاده نمایید.

**URL:** <https://api.sms.ir/v1/send/likeToLike>

**Request Method:** POST

> حداکثر تعداد مجاز شماره‌های مقصد 100 می‌باشد.
> برای ارسال زمان‌بندی شده، انتخاب زمان گذشته نامعتبر می‌باشد.
> برای ارسال زمان‌بندی شده، زمان معتبر می‌تواند در بازه یک ساعت آینده تا حداکثر 365 روز آینده در نظر گرفته شود.

تعداد شماره موبایل‌ها و متن‌های پیامک باید برابر باشند.

#### 3.2.1. پارامترهای بدنه درخواست

| مشخصه        | ارسال   | نوع             | توضیح                                                           |
| ------------ | ------- | --------------- | --------------------------------------------------------------- |
| lineNumber   | اجباری  | Long            | شماره خط ارسالی                                                 |
| MessageTexts | اجباری  | Array of String | متن‌های پیام کوتاه                                              |
| Mobiles      | اجباری  | Array of String | شماره موبایل‌ها                                                  |
| SendDateTime | اختیاری | UnixTime        | زمان ارسال پیامک (در صورت خالی بودن، ارسال در لحظه انجام می‌شود) |

**Request Body:**

```JSON
{
    "lineNumber": "30004505000017",
    "messageTexts": [
        "سرویس پیامکی ایده پردازان با بیش از یک دهه سابقه همراه شماست",
        "ipdemy.ir پلتفرم آموزش آنلاین، آکادمی ایده پردازان"
    ],
    "mobiles": [
        "912xxxx677",
        "+98919xxxx904"
    ]
}
```

#### 3.2.2. مدل دیتای بازگشتی

| مشخصه      | نوع              | توضیح                                |
| ---------- | ---------------- | ------------------------------------ |
| PackId     | Guid             | شناسه یکتای مجموعه ارسال             |
| MessageIds | Array of Integer | آرایه‌ای از شناسه‌های یکتای هر پیامک |
| Cost       | Decimal          | اعتبار مصرفی مجموعه ارسال            |

> در آرایه‌ی `MessageIds`، هر عضو می‌تواند مقدار id متناظر پیامک، `0` یا `null` باشد؛ مقدار `0` به معنای قرارگرفتن شماره در لیست سیاه است و مقدار `null` به معنای نامعتبر بودن شماره یا بیش از حد بودن طول متن برای آن مخاطب است.

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": {
        "packId": "2b99e63c-9bf8-4a21-9bfe-3f72dc1b46f1",
        "messageIds": [
            86522023,
            86522024
        ],
        "cost": 2.0
    }
}
```

#### 3.2.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var payload = @"{" + "\n" +
@"  ""lineNumber"": 300000000000," + "\n" +
@"  ""messageTexts"": [" + "\n" +
@"    ""Your Text 1""" + "\n" +
@"  ]," + "\n" +
@"  ""mobiles"": [" + "\n" +
@"    ""Your Mobile 1""" + "\n" +
@"  ]," + "\n" +
@"  ""sendDateTime"": null" + "\n" +
@"}";
HttpContent content = new StringContent(payload, Encoding.UTF8, "application/json");
var response = await httpClient.PostAsync("https://api.sms.ir/v1/send/likeToLike", content);
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Accept", "text/plain");
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var raw = JSON.stringify({
  "lineNumber": 300000000000,
  "messageTexts": [
    "Your Text 1",
    "Your Text 2"
  ],
  "mobiles": [
    "Your Mobile 1",
    "Your Mobile 1"
  ],
  "senddatetime": null
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/send/likeToLike", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var data = JSON.stringify({
  "lineNumber": 300000000000,
  "messageTexts": [
    "Your Text 1",
    "Your Text 2"
  ],
  "mobiles": [
    "Your Mobile 1",
    "Your Mobile 1"
  ],
  "senddatetime": null
});

var config = {
  method: 'post',
  url: 'https://api.sms.ir/v1/send/likeToLike',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'text/plain',
    'X-API-KEY': 'YOURAPIKEY'
  },
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/send/likeToLike',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "lineNumber": 300000000000,
    "messageTexts": [
        "Your Text 1",
        "Your Text 2"
    ],
    "mobiles": [
        "Your Mobile 1",
        "Your Mobile 1"
    ],
    "senddatetime": null
}',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Accept: text/plain',
    'X-API-KEY: YOURAPIKEY'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = json.dumps({
  "lineNumber": 300000000000,
  "messageTexts": [
    "Your Text 1",
    "Your Text 2"
  ],
  "mobiles": [
    "Your Mobile 1",
    "Your Mobile 1"
  ],
  "senddatetime": None
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'text/plain',
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("POST", "/v1/send/likeToLike", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"lineNumber\": 300000000000,\n
\"messageTexts\": [\n        \"Your Text 1\",\n        \"Your Text 2\"\n    ],\n
  \"mobiles\": [\n        \"Your Mobile 1\",\n        \"Your Mobile 1\"\n    ],\n    \"senddatetime\": null\n}");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/send/likeToLike")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Accept", "text/plain")
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

### 3.3. حذف ارسال زمان‌بندی شده

به منظور حذف و انصراف از ارسال زمان‌بندی شده می‌توانید از متد زیر استفاده نمایید. در این متد، شناسه مجموعه ارسال (packId) دریافتی از خروجی ارسال گروهی یا نظیر به نظیر، مورد استفاده قرار می‌گیرد.

**URL:** <https://api.sms.ir/v1/send/scheduled/{packId}>

**Request Method:** DELETE

> حداکثر تا 3 دقیقه مانده به زمان ارسال زمان‌بندی شده، مجاز به لغو آن می‌باشید.

#### 3.3.1. پارامترهای درخواست

| مشخصه  | ارسال  | نوع  | توضیح              |
| ------ | ------ | ---- | ------------------ |
| PackId | اجباری | Guid | شناسه مجموعه ارسال |

**Request:** <https://api.sms.ir/v1/send/scheduled/2b99e63c-9bf8-4a21-9bfe-3f72dc1b46f1>

#### 3.3.2. مدل دیتای بازگشتی

| مشخصه               | نوع     | توضیح                |
| ------------------- | ------- | -------------------- |
| ReturnedCreditCount | Decimal | مقدار اعتبار بازگشتی |
| SmsCount            | Integer | تعداد پیامک‌ها        |

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": {
      "returnedCreditCount": 10.0,
      "smsCount": 5
    }
}
```

#### 3.3.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.DeleteAsync("https://api.sms.ir/v1/send/scheduled/:Packid");
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("Accept", "text/plain");
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var requestOptions = {
  method: 'DELETE',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/send/scheduled/:Packid", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'delete',
  url: 'https://api.sms.ir/v1/send/scheduled/:Packid',
  headers: {
    'Accept': 'text/plain',
    'X-API-KEY': 'YOURAPIKEY'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/send/scheduled/:Packid',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'DELETE',
  CURLOPT_HTTPHEADER => array(
    'Accept: text/plain',
    'X-API-KEY: YOURAPIKEY'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = ''
headers = {
  'Accept': 'text/plain',
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("DELETE", "/v1/send/scheduled/:Packid", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/send/scheduled/:Packid")
  .method("DELETE", body)
  .addHeader("Accept", "text/plain")
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

### 3.4. ارسال Verify

با استفاده از این متد شما قادر به ارسال پیامک به منظور ارسال کد اعتبارسنجی (verification code)، کد تایید، فاکتور خرید و به طور کلی پیامک‌هایی با اولویت بالا و پارامترهای پویا می‌باشید. از آنجایی که این نوع از ارسال با خطوط خدماتی ارسال می‌شود امکان دریافت آن توسط افرادی که پیامک‌های تبلیغاتی خود را مسدود کرده‌اند نیز وجود دارد و با اولویت بالایی ارسال خواهد شد. برای استفاده از این نوع ارسال ابتدا قالب پیامک خود را در پنل (بخش ارسال سریع) مشخص نمایید.

**URL:** <https://api.sms.ir/v1/send/verify>

**Request Method:** POST

#### 3.4.1. پارامترهای بدنه درخواست

| مشخصه      | ارسال  | نوع                      | توضیح                                                                                                                      |
| ---------- | ------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Mobile     | اجباری | String                   | شماره موبایل                                                                                                               |
| TemplateId | اجباری | Integer                  | شناسه قالب (قالب‌ها از طریق پنل قابل تعریف و مدیریت می‌باشند)                                                               |
| Parameters | اجباری | Array of Parameter Model | آرایه‌ای از مدل Parameter برای تعیین مقادیر جایگزین شونده در قالب تعریف شده (ساختار مدل Parameter در جدول زیر ذکر شده است) |

##### 3.4.1.1. مدل Parameter

| مشخصه | ارسال  | نوع    | توضیح                                                                |
| ----- | ------ | ------ | -------------------------------------------------------------------- |
| Name  | اجباری | String | کلید تعیین شده در قالب (بدون در نظر گرفتن # در ابتدا و انتهای آن)    |
| Value | اجباری | String | مقدار کلید تعیین شده برای جایگزینی در قالب پیامک (حداکثر 25 کاراکتر) |

**Request Body:**

```JSON
{
    "mobile": "919xxxx904",
    "templateId": 123456,
    "parameters": [
      {
        "name": "Code",
        "value": "12345"
      }
    ]
}
```

#### 3.4.2. مدل دیتای بازگشتی

| مشخصه     | نوع     | توضیح              |
| --------- | ------- | ------------------ |
| MessageId | Integer | شناسه یکتای پیامک  |
| Cost      | Decimal | اعتبار مصرفی ارسال |

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": {
        "messageId": 89545112,
        "cost": 1.0
    }
}
```

#### 3.4.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();

httpClient.DefaultRequestHeaders.Add("x-api-key", "5AjUpQILp9t7D2UdaoaJxxxxJdXX0c1dAo456usriKbgyYXqblciFvTm5NLM2346Ipcs");

VerifySendModel model = new VerifySendModel() {
  Mobile = "9120000000",
    TemplateId = 100000,
    Parameters = new VerifySendParameterModel[] {
      new VerifySendParameterModel {
        Name = "CODE", Value = "1234"
      }
    }
};

string payload = JsonSerializer.Serialize(model);
StringContent stringContent = new(payload, Encoding.UTF8, "application/json");

HttpResponseMessage response = await httpClient.PostAsync("https://api.sms.ir/v1/send/verify", stringContent);

public class VerifySendParameterModel
{
    public string Name { get; set; }
    public string Value { get; set; }
}

public class VerifySendModel
{
    public string Mobile { get; set; }

    public int TemplateId { get; set; }

    public VerifySendParameterModel[] Parameters { get; set; }
}
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Accept", "text/plain");
myHeaders.append("x-api-key", "YOURAPIKEY");

  var raw = JSON.stringify({
    "mobile": "Your Mobile",
    "templateId": "YourTemplateID",
    "parameters": [
      {name: 'PARAMETER1' , value: '000000'},
      {name: 'PARAMETER2' , value: '000000'}
    ],
  });

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/send/verify", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var data = JSON.stringify({
    "mobile": "Your Mobile",
    "templateId": "YourTemplateID",
    "parameters": [
      {name: 'PARAMETER1' , value: '000000'},
      {name: 'PARAMETER2' , value: '000000'}
    ],
  });

var config = {
  method: 'post',
  url: 'https://api.sms.ir/v1/send/verify',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'text/plain',
    'x-api-key': 'YOURAPIKEY'
  },
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/send/verify',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
  "mobile": "Your Mobile",
  "templateId": YourTemplateID,
  "parameters": [
    {
      "name": "PARAMETER1",
      "value": "000000"
    },
    {
        "name":"PARAMETER2",
        "value":"000000"
    }
  ]
}',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Accept: text/plain',
    'x-api-key: YOURAPIKEY'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = "{\n  \"mobile\": \"Your Mobile\",\n  \"templateId\": YourTemplateID,\n
  \"parameters\": [\n    {\n      \"name\": \"PARAMETER1\",\n      \"value\": \"000000\"\n    },
  \n    {\n        \"name\":\"PARAMETER2\",\n        \"value\":\"000000\"\n    }\n  ]\n}"
headers = {
  'Content-Type': 'application/json',
  'Accept': 'text/plain',
  'x-api-key': 'YOURAPIKEY'
}
conn.request("POST", "/v1/send/verify", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"mobile\": \"Your Mobile\",\n
  \"templateId\": YourTemplateID,\n
  \"parameters\": [\n    {\n      \"name\": \"PARAMETER1\",\n
    \"value\": \"000000\"\n    },\n    {\n
    \"name\":\"PARAMETER2\",\n
      \"value\":\"000000\"\n    }\n  ]\n}");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/send/verify")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Accept", "text/plain")
  .addHeader("x-api-key", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

### 3.5. ارسال از طریق URL

این متد برای ارسال پیامک از طریق URL مورد استفاده قرار می‌گیرد. برای ارسال کافی است پارامترهای مورد نیاز را در قالب Query Params در آدرس مشخص شده قرار دهید.

**URL:** <https://api.sms.ir/v1/send>

**Request Method:** GET, POST

#### 3.5.1. پارامترهای بدنه درخواست

| مشخصه    | ارسال  | نوع    | توضیح                                                                            |
| -------- | ------ | ------ | -------------------------------------------------------------------------------- |
| Username | اجباری | String | نام کاربری                                                                       |
| Password | اجباری | String | کلید خصوصی (کلیدهای خصوصی شما در پنل برنامه‌نویسان قابل مشاهده و مدیریت می‌باشند.) |
| Line     | اجباری | Long   | شماره خط                                                                         |
| Mobile   | اجباری | String | شماره موبایل                                                                     |
| Text     | اجباری | String | متن پیامک                                                                        |

**Request URL:** <https://api.sms.ir/v1/send?username=MY_USERNAME&password=MY_APIKEY&line=LINE_NUMBER&mobile=MOBILE&text=MESSAGE_TEXT>

#### 3.5.2. مدل دیتای بازگشتی

| مشخصه     | نوع     | توضیح              |
| --------- | ------- | ------------------ |
| MessageId | Integer | شناسه یکتای پیامک  |
| Cost      | Decimal | اعتبار مصرفی ارسال |

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": {
        "messageId": 89545112,
        "cost": 1.0
    }
}
```

#### 3.5.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
var response = await httpClient.GetAsync(
"https://api.sms.ir/v1/send?username=MY_USERNAME&password=MY_APIKEY&mobile=MOBILE&line=LINE_NUMBER&text=MESSAGE_TEXT"
);
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("Accept", "text/plain");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch(
"https://api.sms.ir/v1/send?username=MY_USERNAME&password=MY_APIKEY&mobile=MOBILE&line=LINE_NUMBER&text=MESSAGE_TEXT",
  requestOptions
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/send?username=MY_USERNAME&password=MY_APIKEY&mobile=MOBILE&line=LINE_NUMBER&text=MESSAGE_TEXT',
  headers: {
    'Accept': 'text/plain'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/send?username=MY_USERNAME&password=MY_APIKEY&mobile=MOBILE&line=LINE_NUMBER&text=MESSAGE_TEXT',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Accept: text/plain'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = ''
headers = {
  'Accept': 'text/plain'
}
conn.request(
  "GET",
  "/v1/send?username=MY_USERNAME&password=MY_APIKEY&mobile=MOBILE&line=LINE_NUMBER&text=MESSAGE_TEXT",
  payload,
  headers
  )
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/send?username=MY_USERNAME&password=MY_APIKEY&mobile=MOBILE&line=LINE_NUMBER&text=MESSAGE_TEXT")
  .method("GET", body)
  .addHeader("Accept", "text/plain")
  .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

## 4. گزارش‌ها

### 4.1. گزارش پیامک (دریافت وضعیت)

شما می‌توانید با استفاده از شناسه یکتای پیامک که پس از انجام هریک از ارسال‌ها دریافت کرده‌اید، با فراخوانی این متد، به دریافت اطلاعات پیامک و همینطور اطلاع از وضعیت (Delivery) آن اقدام نمایید.

**URL:** <https://api.sms.ir/v1/send/{messageId}>

**Request Method:** GET

#### 4.1.1. مدل دیتای بازگشتی

| مشخصه            | نوع                         | توضیح             |
| ---------------- | --------------------------- | ----------------- |
| MessageId        | Integer                     | شناسه یکتای پیامک |
| Mobile           | Long                        | شماره موبایل      |
| MessageText      | String                      | متن پیامک         |
| SendDateTime     | Integer (UnixTime)          | زمان ارسال        |
| LineNumber       | Long                        | شماره خط          |
| Cost             | Decimal                     | اعتبار کسر شده    |
| DeliveryState    | Nullable Byte               | وضعیت دلیوری      |
| DeliveryDateTime | Nullable Integer (UnixTime) | زمان دلیوری       |

**Request:** <https://api.sms.ir/v1/send/89545112>

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": {
        "messageId": 89545112,
        "mobile": 912xxxx677,
        "messageText": "سرویس پیامکی ایده پردازان با بیش از یک دهه سابقه همراه شماست",
        "sendDateTime": 1628683626,
        "lineNumber": 30004505000017,
        "cost": 1.0,
        "deliveryState": 1,
        "deliveryDateTime": 1628683629
    }
}
```

#### 4.1.2. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/send/:MessageID");
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/send/:MessageID", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/send/:MessageID',
  headers: {
    'X-API-KEY': 'YOURAPIKEY'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/send/:MessageID',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'X-API-KEY: YOURAPIKEY'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = ''
headers = {
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("GET", "/v1/send/:MessageID", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/send/:MessageID")
  .method("GET", body)
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

### 4.2. گزارش مجموعه ارسال‌های روز

شما می‌توانید با استفاده از این گزارش اطلاعات کلی مجموعه ارسال‌های روز جاری را دریافت نمایید.

**URL:** <https://api.sms.ir/v1/send/pack>

**Request Method:** GET

#### 4.2.1. پارامترهای درخواست

| مشخصه      | ارسال   | نوع     | توضیح                                             |
| ---------- | ------- | ------- | ------------------------------------------------- |
| PageSize   | اختیاری | Integer | تعداد آیتم‌های در صفحه (حداکثر:100 ، پیش‌فرض: 100) |
| PageNumber | اختیاری | Integer | شماره صفحه درخواستی (مقدار پیش‌فرض 1 می‌باشد)       |

**Request:** <https://api.sms.ir/v1/send/pack>

#### 4.2.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)

| مشخصه            | نوع    | توضیح         |
| ---------------- | ------ | ------------- |
| packId           | GUID   | شناسه مجموعه  |
| recipientCount   | Number | تعداد مخاطبان |
| creationDateTime | Number | زمان ایجاد    |

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": [{
        "packId": e7c09e23f0db4834b9bcb79e7b054f4c,
        "recipientCount": 100,
        "creationDateTime": 1628683626,
    },{
       "packId": 0cf3017fd9d84babbb5ed5579104dab2,
        "recipientCount": 200,
        "creationDateTime": 1628683626,
    }]
}
```

#### 4.2.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/send/pack?pageNumber=1&pageSize=100");
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("Accept", "text/plain");
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/send/pack?pageNumber=1&pageSize=100", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/send/pack?pageNumber=1&pageSize=100',
  headers: {
    'Accept': 'text/plain',
    'X-API-KEY': 'YOURAPIKEY'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/send/pack?pageNumber=1&pageSize=100',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Accept: text/plain',
    'X-API-KEY: YOURAPIKEY',
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = ''
headers = {
  'Accept': 'text/plain',
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("GET", "/v1/send/pack?pageNumber=1&pageSize=100", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/send/pack?pageNumber=1&pageSize=100")
  .method("GET", body)
  .addHeader("Accept", "text/plain")
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

### 4.3. گزارش مجموعه ارسال

شما می‌توانید با استفاده از شناسه مجموعه ارسال، گزارشی از پیامک‌های ارسالی در آن درخواست به همراه وضعیت‌هایشان را دریافت نمایید.

**URL:** <https://api.sms.ir/v1/send/pack/{packId}>

**Request Method:** GET

#### 4.3.1. پارامترهای درخواست

| مشخصه  | ارسال  | نوع  | توضیح              |
| ------ | ------ | ---- | ------------------ |
| PackId | اجباری | Guid | شناسه مجموعه ارسال |

**Request:** <https://api.sms.ir/v1/send/pack/bdec19c9-2736-4095-8ef1-ea21afe3771f>

#### 4.3.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)

| مشخصه            | نوع                         | توضیح             |
| ---------------- | --------------------------- | ----------------- |
| MessageId        | Integer                     | شناسه یکتای پیامک |
| Mobile           | Long                        | شماره موبایل      |
| MessageText      | String                      | متن پیامک         |
| SendDateTime     | Integer (UnixTime)          | زمان ارسال        |
| LineNumber       | Long                        | شماره خط          |
| Cost             | Decimal                     | اعتبار کسر شده    |
| DeliveryState    | Nullable Byte               | وضعیت دلیوری      |
| DeliveryDateTime | Nullable Integer (UnixTime) | زمان دلیوری       |

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": [{
        "messageId": 89545112,
        "mobile": 912xxxx677,
        "messageText": "سرویس پیامکی ایده پردازان با بیش از یک دهه سابقه همراه شماست",
        "sendDateTime": 1628683626,
        "lineNumber": 30004505000017,
        "cost": 1.0,
        "deliveryState": 1,
        "deliveryDateTime": 1628683629
    },{
        "messageId": 89545113,
        "mobile": 919xxxx378,
        "messageText": "ipdemy.ir پلتفرم آموزش آنلاین، آکادمی ایده پردازان",
        "sendDateTime": 1628683626,
        "lineNumber": 30004505000017,
        "cost": 1.0,
        "deliveryState": 3,
        "deliveryDateTime": 1628683625
    }]
}
```

#### 4.3.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/send/pack/:PackID");
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("PageSize", "2");
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/send/pack/:PackID", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/send/pack/:PackID',
  headers: {
    'PageSize': '2',
    'X-API-KEY': 'YOURAPIKEY'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/send/pack/:PackID',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'PageSize: 2',
    'X-API-KEY: YOURAPIKEY'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = ''
headers = {
  'PageSize': '2',
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("GET", "/v1/send/pack/:PackID", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/send/pack/:PackID")
  .method("GET", body)
  .addHeader("PageSize", "2")
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

### 4.4. گزارش ارسال‌های روز

با استفاده از متد زیر، گزارشی از ارسال‌های انجام شده در روز جاری قابل دریافت است.

**URL:** <https://api.sms.ir/v1/send/live>

**Request Method:** GET

#### 4.4.1. پارامترهای درخواست

| مشخصه      | ارسال   | نوع     | توضیح                                             |
| ---------- | ------- | ------- | ------------------------------------------------- |
| PageSize   | اختیاری | Integer | تعداد آیتم‌های در صفحه (حداکثر:100 ، پیش‌فرض: 100) |
| PageNumber | اختیاری | Integer | شماره صفحه درخواستی (مقدار پیش‌فرض 1 می‌باشد)       |

**Request:** <https://api.sms.ir/v1/send/live?pageSize=25&pageNumber=3>

#### 4.4.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)

| مشخصه            | نوع                         | توضیح             |
| ---------------- | --------------------------- | ----------------- |
| MessageId        | Integer                     | شناسه یکتای پیامک |
| Mobile           | Long                        | شماره موبایل      |
| MessageText      | String                      | متن پیامک         |
| SendDateTime     | Integer (UnixTime)          | زمان ارسال        |
| LineNumber       | Long                        | شماره خط          |
| Cost             | Decimal                     | اعتبار کسر شده    |
| DeliveryState    | Nullable Byte               | وضعیت دلیوری      |
| DeliveryDateTime | Nullable Integer (UnixTime) | زمان دلیوری       |

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": [{
        "messageId": 89545112,
        "mobile": 912xxxx677,
        "messageText": "سرویس پیامکی ایده پردازان با بیش از یک دهه سابقه همراه شماست",
        "sendDateTime": 1628683626,
        "lineNumber": 30004505000017,
        "cost": 1.0,
        "deliveryState": 1,
        "deliveryDateTime": 1628683629
    },{
        "messageId": 89545113,
        "mobile": 919xxxx378,
        "messageText": "ipdemy.ir پلتفرم آموزش آنلاین، آکادمی ایده پردازان",
        "sendDateTime": 1628683626,
        "lineNumber": 30004505000017,
        "cost": 1.0,
        "deliveryState": 3,
        "deliveryDateTime": 1628683625
    }]
}
```

#### 4.4.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/send/live?pageNumber=1&pageSize=100");
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("Accept", "text/plain");
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/send/live?pageNumber=1&pageSize=20", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/send/live?pageNumber=1&pageSize=20',
  headers: {
    'Accept': 'text/plain',
    'X-API-KEY': 'YOURAPIKEY'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/send/live?pageNumber=1&pageSize=20',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Accept: text/plain',
    'X-API-KEY: YOURAPIKEY'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = ''
headers = {
  'Accept': 'text/plain',
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("GET", "/v1/send/live?pageNumber=1&pageSize=20", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/send/live?pageNumber=1&pageSize=20")
  .method("GET", body)
  .addHeader("Accept", "text/plain")
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

### 4.5. گزارش ارسال‌های آرشیو شده

با فراخوانی متد زیر، گزارشی از ارسال‌های انجام شده در گذشته (تا انتهای روز قبل)، را دریافت خواهید نمود.

**URL:** <https://api.sms.ir/v1/send/archive>

**Request Method:** GET

#### 4.5.1. پارامترهای درخواست

| مشخصه      | ارسال   | نوع                | توضیح                                             |
| ---------- | ------- | ------------------ | ------------------------------------------------- |
| FromDate   | اختیاری | Integer (UnixTime) | از تاریخ                                          |
| ToDate     | اختیاری | Integer (UnixTime) | تا تاریخ                                          |
| PageSize   | اختیاری | Integer            | تعداد آیتم‌های در صفحه (حداکثر:100 ، پیش‌فرض: 100) |
| PageNumber | اختیاری | Integer            | شماره صفحه درخواستی (مقدار پیش‌فرض 1 می‌باشد)       |

**Request:** <https://api.sms.ir/v1/send/archive?fromDate=1613465574&toDate=1623805200>

#### 4.5.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)

| مشخصه            | نوع                         | توضیح             |
| ---------------- | --------------------------- | ----------------- |
| MessageId        | Integer                     | شناسه یکتای پیامک |
| Mobile           | Long                        | شماره موبایل      |
| MessageText      | String                      | متن پیامک         |
| SendDateTime     | Integer (UnixTime)          | زمان ارسال        |
| LineNumber       | Long                        | شماره خط          |
| Cost             | Decimal                     | اعتبار کسر شده    |
| DeliveryState    | Nullable Byte               | وضعیت دلیوری      |
| DeliveryDateTime | Nullable Integer (UnixTime) | زمان دلیوری       |

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": [{
        "messageId": 89545112,
        "mobile": 912xxxx677,
        "messageText": "سرویس پیامکی ایده پردازان با بیش از یک دهه سابقه همراه شماست",
        "sendDateTime": 1628583626,
        "lineNumber": 30004505000017,
        "cost": 1.0,
        "deliveryState": 1,
        "deliveryDateTime": 1628683629
    },{
        "messageId": 89545113,
        "mobile": 919xxxx378,
        "messageText": "ipdemy.ir پلتفرم آموزش آنلاین، آکادمی ایده پردازان",
        "sendDateTime": 1628583626,
        "lineNumber": 30004505000017,
        "cost": 1.0,
        "deliveryState": 3,
        "deliveryDateTime": 1628683625
    },{
        "messageId": 89545114,
        "mobile": 921xxxx432,
        "messageText": "HyperBox.irفروشگاه اینترنتی اسباب بازی و عروسک ",
        "sendDateTime": 1628583626,
        "lineNumber": 30004505000017,
        "cost": 1.0,
        "deliveryState": 1,
        "deliveryDateTime": 1628683669
    }]
}
```

#### 4.5.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/send/archive?pageNumber=1&pageSize=100&fromDate=1669753800&toDate=1672814257");
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("Accept", "text/plain");
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/send/archive?pageNumber=1&pageSize=100&fromDate=1650016645&toDate=1650880645", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/send/archive?pageNumber=1&pageSize=100&fromDate=1650016645&toDate=1650880645',
  headers: {
    'Accept': 'text/plain',
    'X-API-KEY': 'YOURAPIKEY'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/send/archive?pageNumber=1&pageSize=100&fromDate=1650016645&toDate=1650880645',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Accept: text/plain',
    'X-API-KEY: YOURAPIKEY'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = ''
headers = {
  'Accept': 'text/plain',
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("GET", "/v1/send/archive?pageNumber=1&pageSize=100&fromDate=1650016645&toDate=1650880645", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/send/archive?pageNumber=1&pageSize=100&fromDate=1650016645&toDate=1650880645")
  .method("GET", body)
  .addHeader("Accept", "text/plain")
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

### 4.6. گزارش تازه‌ترین پیامک‌های دریافتی

شما می‌توانید با استفاده از این متد، تازه‌ترین پیامک‌های دریافتی را مشاهده نمایید. لازم به ذکر است هر پیامک دریافتی تنها یک مرتبه توسط این متد قابل دستیابی می‌باشد و پس از آن به دلیل قرار گرفتن در حالت خوانده شده قابل دسترسی مجدد توسط این متد نمی‌باشند.

**URL:** <https://api.sms.ir/v1/receive/latest>

**Request Method:** GET

#### 4.6.1. پارامترهای درخواست

| مشخصه | ارسال   | نوع     | توضیح                                                            |
| ----- | ------- | ------- | ---------------------------------------------------------------- |
| Count | اختیاری | Integer | تعداد درخواستی (حداکثر تعداد درخواستی و مقدار پیش‌فرض 100 می‌باشد) |

**Request:** <https://api.sms.ir/v1/receive/latest?count=50>

#### 4.6.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)

| مشخصه            | نوع                | توضیح                     |
| ---------------- | ------------------ | ------------------------- |
| ReceiveReturnId  | Long               | شناسه یکتای پیامک دریافتی |
| MessageText      | String             | متن پیامک                 |
| Number           | Long               | شماره خط دریافت‌کننده      |
| Mobile           | Long               | شماره موبایل ارسال کننده  |
| ReceivedDateTime | Integer (UnixTime) | زمان دریافت               |

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": [
        {
            "receiveReturnId": 123456789,
            "messageText": "HyperBox.irفروشگاه اینترنتی اسباب بازی و عروسک",
            "number": 30004505000017,
            "mobile": 912xxxx002,
            "receivedDateTime": 1628683625
        }
    ]
}
```

#### 4.6.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/receive/latest?count=100");
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/receive/latest?count=100", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/receive/latest?count=100',
  headers: {
    'X-API-KEY': 'YOURAPIKEY'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/receive/latest?count=100',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'X-API-KEY: YOURAPIKEY'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = ''
headers = {
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("GET", "/v1/receive/latest?count=100", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/receive/latest?count=100")
  .method("GET", body)
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

### 4.7. گزارش پیامک‌های دریافتی روز

با فراخوانی متد زیر، گزارش پیامک‌های دریافتی روز جاری (اعم از خوانده شده و نشده) قابل دستیابی می‌باشد.

> در آغازین ساعات روز، گزارش پیام‌های دریافتی روز گذشته نیز با فراخوانی این متد قابل دریافت می‌باشد.

**URL:** <https://api.sms.ir/v1/receive/live>

**Request Method:** GET

#### 4.7.1. پارامترهای درخواست

| مشخصه        | ارسال   | نوع     | توضیح                                                                  |
| ------------ | ------- | ------- | ---------------------------------------------------------------------- |
| PageSize     | اختیاری | Integer | تعداد آیتم‌های در صفحه (حداکثر:100 ، پیش‌فرض: 100)                      |
| PageNumber   | اختیاری | Integer | شماره صفحه درخواستی (مقدار پیش‌فرض 1 می‌باشد)                            |
| sortByNewest | اختیاری | Boolean | مرتب‌سازی بر اساس تاریخ دریافت (پیش‌فرض به صورت صعودی، با مقدار False) |
| mobile       | اختیاری | String  | شماره موبایل ارسال کننده پیامک                                         |

**Request:** <https://api.sms.ir/v1/receive/live?pageSize=20&pageNumber=3&sortByNewest=false>

#### 4.7.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)

| مشخصه            | نوع                | توضیح                    |
| ---------------- | ------------------ | ------------------------ |
| Mobile           | Long               | شماره موبایل ارسال کننده |
| MessageText      | String             | متن پیامک                |
| Number           | Long               | شماره خط دریافت‌کننده     |
| ReceivedDateTime | Integer (UnixTime) | زمان دریافت              |

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": [
        {
            "messageText": "HyperBox.irفروشگاه اینترنتی اسباب بازی و عروسک",
            "number": 30004505000017,
            "mobile": 912xxxx002,
            "receivedDateTime": 1628683625
        }
    ]
}
```

#### 4.7.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/receive/live?pageNumber=1&pageSize=100");
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("PageSize", "2");
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/receive/live?pageNumber=1&pageSize=100", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/receive/live?pageNumber=1&pageSize=100',
  headers: {
    'PageSize': '2',
    'X-API-KEY': 'YOURAPIKEY'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/receive/live?pageNumber=1&pageSize=100',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'PageSize: 2',
    'X-API-KEY: YOURAPIKEY'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = ''
headers = {
  'PageSize': '2',
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("GET", "/v1/receive/live?pageNumber=1&pageSize=100", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/receive/live?pageNumber=1&pageSize=100")
  .method("GET", body)
  .addHeader("PageSize", "2")
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

### 4.8. گزارش پیامک‌های دریافتی آرشیو شده

با فراخوانی متد زیر، گزارشی از پیامک‌های دریافتی در گذشته (تا انتهای روز قبل)، را مشاهده خواهید نمود.

**URL:** <https://api.sms.ir/v1/receive/archive>

**Request Method:** GET

#### 4.8.1. پارامترهای درخواست

| مشخصه      | ارسال   | نوع                | توضیح                                             |
| ---------- | ------- | ------------------ | ------------------------------------------------- |
| FromDate   | اختیاری | Integer (UnixTime) | از تاریخ                                          |
| ToDate     | اختیاری | Integer (UnixTime) | تا تاریخ                                          |
| PageSize   | اختیاری | Integer            | تعداد آیتم‌های در صفحه (حداکثر:100 ، پیش‌فرض: 100) |
| PageNumber | اختیاری | Integer            | شماره صفحه درخواستی (مقدار پیش‌فرض 1 می‌باشد)       |
| mobile     | اختیاری | String             | شماره موبایل ارسال کننده پیامک                    |

**Request:** <https://api.sms.ir/v1/receive/archive?fromDate=1613465574&toDate=1623805200>

#### 4.8.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)

| مشخصه            | نوع                | توضیح                    |
| ---------------- | ------------------ | ------------------------ |
| ReceiveReturnId  | Long               | شناسه پیامک دریافتی      |
| MessageText      | String             | متن پیامک                |
| Number           | Long               | شماره خط دریافت‌کننده     |
| Mobile           | Long               | شماره موبایل ارسال کننده |
| ReceivedDateTime | Integer (UnixTime) | زمان دریافت              |

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": [
        {
            "receiveReturnId": 12345678987,
            "messageText": "HyperBox.irفروشگاه اینترنتی اسباب بازی و عروسک",
            "number": 30004505000017,
            "mobile": 912xxxx002,
            "receivedDateTime": 1628683625
        }
    ]
}
```

#### 4.8.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/receive/archive?pageNumber=1&pageSize=100&fromDate=1669753800&toDate=1672814257");
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("PageSize", "2");
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/receive/archive?pageNumber=1&pageSize=100&fromDate=1628683629&toDate=1628693629", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/receive/archive?pageNumber=1&pageSize=100&fromDate=1628683629&toDate=1628693629',
  headers: {
    'PageSize': '2',
    'X-API-KEY': 'YOURAPIKEY'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/receive/archive?pageNumber=1&pageSize=100&fromDate=1628683629&toDate=1628693629',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'PageSize: 2',
    'X-API-KEY: YOURAPIKEY'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = ''
headers = {
  'PageSize': '2',
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("GET", "/v1/receive/archive?pageNumber=1&pageSize=100&fromDate=1628683629&toDate=1628693629", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/receive/archive?pageNumber=1&pageSize=100&fromDate=1628683629&toDate=1628693629")
  .method("GET", body)
  .addHeader("PageSize", "2")
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

## 5. تنظیمات

### 5.1. دریافت مقدار اعتبار فعلی

برای مشاهده مقدار اعتبار فعلی از متد زیر استفاده نمایید.

**URL:** <https://api.sms.ir/v1/credit>

**Request Method:** GET

> ⚠️ **نکته:** با اینکه این متد در مستندات رسمی sms.ir با عنوان «اعتبار» (credit) معرفی شده، مقدار بازگشتی آن در عمل **تعداد پیامک باقی‌مانده** حساب شماست، نه مبلغ اعتبار ریالی. این نکته در مستندات رسمی ذکر نشده و بر اساس آزمایش عملی مشخص شده است؛ در صورت مشاهده رفتار متفاوت، مقادیر واقعی حساب خودتان را نیز بررسی کنید.

#### 5.1.1. دیتای بازگشتی

| نوع     | توضیح                    |
| ------- | ------------------------ |
| Decimal | تعداد پیامک باقی‌مانده   |

**Request:** <https://api.sms.ir/v1/credit>

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": 165.3
}
```

#### 5.1.2. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/credit");
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/credit", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/credit',
  headers: {
    'X-API-KEY': 'YOURAPIKEY'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/credit',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'X-API-KEY: YOURAPIKEY'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = ''
headers = {
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("GET", "/v1/credit", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/credit")
  .method("GET", body)
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

### 5.2. دریافت لیست خطوط

با استفاده از این متد، لیست خطوط آماده استفاده برای ارسال، قابل مشاهده است.

**URL:** <https://api.sms.ir/v1/line>

**Request Method:** GET

#### 5.2.1. دیتای بازگشتی (آرایه‌ای از Long)

| نوع  | توضیح    |
| ---- | -------- |
| Long | شماره خط |

**Request:** <https://api.sms.ir/v1/line>

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": [10002155613464, 30004505000017]
}
```

#### 5.2.2. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/line");
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("PageSize", "2");
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/line", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/line',
  headers: {
    'PageSize': '2',
    'X-API-KEY': 'YOURAPIKEY'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/line',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'PageSize: 2',
    'X-API-KEY: YOURAPIKEY'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = ''
headers = {
  'PageSize': '2',
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("GET", "/v1/line", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/line")
  .method("GET", body)
  .addHeader("PageSize", "2")
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

---

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](#73-جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

## 6. جداول کدهای وضعیت

### 6.1. کدهای وضعیت‌

| کد وضعیت | توضیح                                                                                   |
| -------- | --------------------------------------------------------------------------------------- |
| 0        | درخواست شما با خطا مواجه شده‌است.                                                        |
| 1        | عملیات با موفقیت انجام شد                                                               |
| 10       | کلید وب سرویس نامعتبر است                                                               |
| 11       | کلید وب سرویس غیرفعال است                                                               |
| 12       | کلید وب سرویس محدود به آی‌پی‌های تعریف شده می‌باشد.                                        |
| 13       | حساب کاربری غیرفعال است                                                                 |
| 14       | حساب کاربری در حالت تعلیق قرار دارد                                                     |
| 15       | به منظور استفاده از وب سرویس پلن خود را ارتقا دهید                                      |
| 16       | مقدار ارسالی پارامتر نادرست می‌باشد                                                      |
| 20       | تعداد درخواست بیشتر از حد مجاز است                                                      |
| 101      | شماره خط نامعتبر می‌باشد                                                                 |
| 102      | اعتبار کافی نمی‌باشد                                                                     |
| 103      | درخواست شما دارای متن (های) خالی است                                                    |
| 104      | درخواست شما دارای موبایل (های) نادرست است                                               |
| 105      | تعداد موبایل‌ها بیشتر از حد مجاز (100 عدد) می‌باشد                                       |
| 106      | تعداد متن‌ها بیشتر از حد مجاز (100 عدد) می‌باشد                                          |
| 107      | لیست موبایل‌ها خالی می‌باشد                                                              |
| 108      | لیست متن‌ها خالی می‌باشد                                                                 |
| 109      | زمان ارسال نامعتبر می‌باشد                                                               |
| 110      | تعداد شماره موبایل‌ها و تعداد متن‌ها برابر نیستند                                       |
| 111      | با این شناسه ارسالی ثبت نشده است                                                        |
| 112      | رکوردی برای حذف یافت نشد                                                                |
| 113      | قالب یافت نشد                                                                           |
| 114      | طول رشته مقدار پارامتر، بیش از حد مجاز (25 کاراکتر) می‌باشد                              |
| 115      | شماره موبایل(ها) در لیست سیاه سامانه می‌باشند                                            |
| 116      | نام یک یا چند پارامتر مقداردهی نشده‌است. لطفا به بخش مستندات ارسال وریفای مراجعه فرمایید |
| 117      | متن ارسال شده مورد تایید نمی‌باشد                                                        |
| 118      | تعداد پیام‌ها بیشتر از حد مجاز می‌باشد                                                   |
| 119      | به منظور استفاده از قالب شخصی‌سازی‌شده پلن خود را ارتقا دهید                            |
| 123      | خط ارسال‌کننده نیاز به فعال‌سازی دارد.                                                    |
| 124      | درحال حاضر، فقط امکان ارسال پیامک OTP وجود دارد و قالب شما OTP شناسایی نشده است!        |

### 6.2. کدهای وضعیت دلیوری

| کد وضعیت | توضیح             |
| -------- | ----------------- |
| 1        | رسیده             |
| 2        | نرسیده به گوشی    |
| 3        | رسیده به مخابرات  |
| 4        | نرسیده به مخابرات |
| 5        | رسیده به اپراتور  |
| 6        | ناموفق            |
| 7        | لیست سیاه         |
| 8        | نامشخص            |

---

## 7. کتابخانه‌های رسمی (SDK)

علاوه بر فراخوانی مستقیم REST API، تیم sms.ir کتابخانه‌های رسمی (SDK) برای چند زبان و فریم‌ورک پرکاربرد منتشر کرده که همان متدهای این مستند را به‌صورت آماده و تایپ‌شده در اختیار قرار می‌دهند. فهرست این پکیج‌ها در صفحه [پکیج‌های وب سرویس](https://sms.ir/web-service/پکیج-های-وب-سرویس/) سایت sms.ir نیز آمده است.

### 7.1. فهرست پکیج‌ها

| زبان / فریم‌ورک | مخزن گیت‌هاب                                                                     | نصب                                  |
| ---------------- | --------------------------------------------------------------------------------- | ------------------------------------ |
| Node.js           | [SmsPanelV2.nodejs](https://github.com/IPeCompany/SmsPanelV2.nodejs)              | `npm install smsir-js`               |
| PHP / Laravel     | [smsir-php](https://github.com/IPeCompany/smsir-php)                              | `composer require ipe/smsir-php`     |
| TypeScript        | [SmsPanelV2.TypeScript](https://github.com/IPeCompany/SmsPanelV2.TypeScript)      | `npm install sms-typescript`         |
| .NET              | [SmsPanelV2.dotNet](https://github.com/IPeCompany/SmsPanelV2.dotNet)              | `dotnet add package IPE.SmsIR`       |
| Python            | [SmsPanelV2.Python](https://github.com/IPeCompany/SmsPanelV2.Python)              | `pip install smsir-python`           |

> در تمام پکیج‌ها، کلید API همان کلیدی است که طبق [بخش ۱.۵](#15-authorization--احراز-هویت) از پنل برنامه‌نویسان دریافت می‌کنید.

### 7.2. شروع سریع به تفکیک زبان

**Node.js ([smsir-js](https://github.com/IPeCompany/SmsPanelV2.nodejs))**

```js
const { Smsir } = require('smsir-js')

const smsir = new Smsir(api_key, line_number)

// ارسال گروهی
smsir.SendBulk(messageText, mobiles, sendDateTime, lineNumber)

// ارسال Verify
smsir.SendVerifyCode(mobile, templateId, parameters)
```

**PHP / Laravel ([smsir-php](https://github.com/IPeCompany/smsir-php))**

```php
use Ipe\Sdk\Facades\SmsIr;

// ارسال گروهی
$response = SmsIr::bulkSend($lineNumber, $messageText, $mobiles, $sendDateTime);

// ارسال Verify
$response = SmsIr::verifySend($mobile, $templateId, $parameters);
```

**TypeScript ([sms-typescript](https://github.com/IPeCompany/SmsPanelV2.TypeScript))**

```ts
import { Smsir } from "sms-typescript";

const sms = new Smsir("your-api-key", lineNumber);

// ارسال گروهی
const result = await sms.sendBulk("متن پیام", ["09123456789"]);

// ارسال Verify
await sms.sendVerifyCode("09123456789", templateId, [
  { name: "Code", value: "123456" },
]);
```

**.NET ([IPE.SmsIr](https://github.com/IPeCompany/SmsPanelV2.dotNet))**

```csharp
SmsIr smsIr = new SmsIr("YOUR API KEY");

// ارسال گروهی
var bulkResult = await smsIr.BulkSendAsync(lineNumber, messageText, mobiles, sendDateTime);

// ارسال Verify
var verifyResult = await smsIr.VerifySendAsync(mobile, templateId, verifySendParameters);
```

**Python ([smsir-python](https://github.com/IPeCompany/SmsPanelV2.Python))**

```python
from sms_ir import SmsIr

sms_ir = SmsIr(api_key, linenumber)

# ارسال گروهی
sms_ir.send_bulk_sms(numbers, message, linenumber)

# ارسال Verify
sms_ir.send_verify_code(number, template_id, parameters)
```

### 7.3. جدول تناظر متدهای API با متدهای هر SDK

| متد API (این مستند)                              | Node.js                | PHP / Laravel                | TypeScript             | .NET                        | Python                      |
| -------------------------------------------------- | ----------------------- | ------------------------------ | ------------------------ | ----------------------------- | ------------------------------ |
| [3.1. ارسال گروهی](#31-ارسال-گروهی)             | `SendBulk`               | `bulkSend`                      | `sendBulk`                | `BulkSendAsync`                 | `send_bulk_sms`                  |
| [3.2. ارسال نظیر به نظیر](#32-ارسال-نظیر-به-نظیر) | `SendLikeToLike`         | `likeToLikeSend`                | `sendLikeToLike`          | `LikeToLikeSendAsync`           | `send_like_to_like`              |
| [3.3. حذف ارسال زمان‌بندی شده](#33-حذف-ارسال-زمانبندی-شده) | `deleteScheduled`       | `removeScheduledMessages`       | `deleteScheduled`          | `RemoveScheduledMessagesAsync`  | `delete_scheduled`               |
| [3.4. ارسال Verify](#34-ارسال-verify)          | `SendVerifyCode`          | `verifySend`                     | `sendVerifyCode`           | `VerifySendAsync`                | `send_verify_code`                |
| [3.5. ارسال از طریق URL](#35-ارسال-از-طریق-url) | در README مستند نشده     | در README مستند نشده             | `sendByURL`                | در README مستند نشده             | در README مستند نشده              |
| [4.1. گزارش پیامک](#41-گزارش-پیامک-دریافت-وضعیت)   | `ReportMessage`           | `getReportByMessageId`           | `reportMessage`            | `GetReportAsync`                 | `report_message`                  |
| [4.2. گزارش مجموعه ارسال‌های روز](#42-گزارش-مجموعه-ارسالهای-روز) | در README مستند نشده     | `getSendPacks`                   | `reportDailyPack`          | `GetSendPacksAsync`              | در README مستند نشده              |
| [4.3. گزارش مجموعه ارسال](#43-گزارش-مجموعه-ارسال) | `ReportPack`              | `getReportByPackId`              | `reportPackById`           | `GetReportAsync` (overload)      | `report_pack`                     |
| [4.4. گزارش ارسال‌های روز](#44-گزارش-ارسالهای-روز) | `ReportToday`             | `getLiveReport`                  | `reportTodayLive`          | `GetLiveReportAsync`             | `report_today`                    |
| [4.5. گزارش ارسال‌های آرشیو شده](#45-گزارش-ارسالهای-آرشیو-شده) | `ReportArchived`          | `getArchivedReport`              | `reportArchive`            | `GetArchivedReportAsync`         | `report_archived`                 |
| [4.6. گزارش تازه‌ترین پیامک‌های دریافتی](#46-گزارش-تازهترین-پیامکهای-دریافتی) | `ReportLatestReceived`    | `getLatestReceives`              | `reportLatestReceive`      | `GetLatestReceivesAsync`         | `report_latest_received`          |
| [4.7. گزارش پیامک‌های دریافتی روز](#47-گزارش-پیامکهای-دریافتی-روز) | `ReportTodayReceived`     | `getLiveReceives`                | `reportReceiveLive`        | `GetLiveReceivesAsync`           | `report_today_received`           |
| [4.8. گزارش پیامک‌های دریافتی آرشیو شده](#48-گزارش-پیامکهای-دریافتی-آرشیو-شده) | `ReportArchivedReceived`  | `getArchivedReceives`            | `reportReceiveArchive`     | `GetArchivedReceivesAsync`       | `report_archived_received`        |
| [5.1. دریافت مقدار اعتبار فعلی](#51-دریافت-مقدار-اعتبار-فعلی) | `getCredit`               | `getCredit`                      | `getCredit`                | `GetCreditAsync`                 | `get_credit`                      |
| [5.2. دریافت لیست خطوط](#52-دریافت-لیست-خطوط)     | `getLineNumbers`          | `getLines`                       | `getLineNumbers`           | `GetLinesAsync`                  | `get_line_numbers`                |

> ستون‌هایی که «در README مستند نشده» ذکر شده‌اند، به این معنا نیست که آن قابلیت در پکیج وجود ندارد؛ صرفاً در فایل README مخزن مربوطه، متد معادل آن به‌صراحت ذکر نشده است. برای اطمینان، به سورس‌کد پکیج یا Issues مخزن مراجعه کنید.

### 7.4. لایسنس و پشتیبانی

تمام پکیج‌های فوق به‌صورت متن‌باز (عمدتاً با مجوز MIT) در گیت‌هاب سازمان [IPeCompany](https://github.com/IPeCompany) نگهداری می‌شوند. برای گزارش باگ یا درخواست قابلیت جدید، بخش Issues همان مخزن مناسب‌ترین مسیر است؛ برای پرسش‌های مربوط به خود وب‌سرویس (کلید API، اعتبار، خطوط و ...) با پشتیبانی sms.ir در تماس باشید.
