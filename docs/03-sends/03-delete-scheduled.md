# 3.3. حذف ارسال زمان‌بندی شده

به منظور حذف و انصراف از ارسال زمان‌بندی شده می‌توانید از متد زیر استفاده نمایید. در این متد، شناسه مجموعه ارسال (packId) دریافتی از خروجی ارسال گروهی یا نظیر به نظیر، مورد استفاده قرار می‌گیرد.

**URL:** <https://api.sms.ir/v1/send/scheduled/{packId}>

**Request Method:** DELETE

> حداکثر تا 3 دقیقه مانده به زمان ارسال زمان‌بندی شده، مجاز به لغو آن می‌باشید.

## 3.3.1. پارامترهای درخواست

| مشخصه  | ارسال  | نوع  | توضیح              |
| ------ | ------ | ---- | ------------------ |
| PackId | اجباری | Guid | شناسه مجموعه ارسال |

**Request:** <https://api.sms.ir/v1/send/scheduled/2b99e63c-9bf8-4a21-9bfe-3f72dc1b46f1>

## 3.3.2. مدل دیتای بازگشتی

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

## 3.3.3. نمونه کد

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

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](../07-sdks/README.md#جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

---

[بازگشت به فهرست مطالب](../README.md)
