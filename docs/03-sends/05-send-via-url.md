# 3.5. ارسال از طریق URL

این متد برای ارسال پیامک از طریق URL مورد استفاده قرار می‌گیرد. برای ارسال کافی است پارامترهای مورد نیاز را در قالب Query Params در آدرس مشخص شده قرار دهید.

**URL:** <https://api.sms.ir/v1/send>

**Request Method:** GET, POST

## 3.5.1. پارامترهای بدنه درخواست

| مشخصه    | ارسال  | نوع    | توضیح                                                                            |
| -------- | ------ | ------ | -------------------------------------------------------------------------------- |
| Username | اجباری | String | نام کاربری                                                                       |
| Password | اجباری | String | کلید خصوصی (کلیدهای خصوصی شما در پنل برنامه‌نویسان قابل مشاهده و مدیریت می‌باشند.) |
| Line     | اجباری | Long   | شماره خط                                                                         |
| Mobile   | اجباری | String | شماره موبایل                                                                     |
| Text     | اجباری | String | متن پیامک                                                                        |

**Request URL:** <https://api.sms.ir/v1/send?username=MY_USERNAME&password=MY_APIKEY&line=LINE_NUMBER&mobile=MOBILE&text=MESSAGE_TEXT>

## 3.5.2. مدل دیتای بازگشتی

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

## 3.5.3. نمونه کد

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

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](../07-sdks/README.md#جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

---

[بازگشت به فهرست مطالب](../README.md)
