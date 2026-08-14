# 4.1. گزارش پیامک (دریافت وضعیت)

شما می‌توانید با استفاده از شناسه یکتای پیامک که پس از انجام هریک از ارسال‌ها دریافت کرده‌اید، با فراخوانی این متد، به دریافت اطلاعات پیامک و همینطور اطلاع از وضعیت (Delivery) آن اقدام نمایید.

**URL:** <https://api.sms.ir/v1/send/{messageId}>

**Request Method:** GET

## 4.1.1. مدل دیتای بازگشتی

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

## 4.1.2. نمونه کد

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

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](../07-sdks/README.md#جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

---

[بازگشت به فهرست مطالب](../README.md)
