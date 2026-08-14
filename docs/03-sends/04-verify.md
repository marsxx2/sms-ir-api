# 3.4. ارسال Verify

با استفاده از این متد شما قادر به ارسال پیامک به منظور ارسال کد اعتبارسنجی (verification code)، کد تایید، فاکتور خرید و به طور کلی پیامک‌هایی با اولویت بالا و پارامترهای پویا می‌باشید. از آنجایی که این نوع از ارسال با خطوط خدماتی ارسال می‌شود امکان دریافت آن توسط افرادی که پیامک‌های تبلیغاتی خود را مسدود کرده‌اند نیز وجود دارد و با اولویت بالایی ارسال خواهد شد. برای استفاده از این نوع ارسال ابتدا قالب پیامک خود را در پنل (بخش ارسال سریع) مشخص نمایید.

**URL:** <https://api.sms.ir/v1/send/verify>

**Request Method:** POST

## 3.4.1. پارامترهای بدنه درخواست

| مشخصه      | ارسال  | نوع                      | توضیح                                                                                                                      |
| ---------- | ------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Mobile     | اجباری | String                   | شماره موبایل                                                                                                               |
| TemplateId | اجباری | Integer                  | شناسه قالب (قالب‌ها از طریق پنل قابل تعریف و مدیریت می‌باشند)                                                               |
| Parameters | اجباری | Array of Parameter Model | آرایه‌ای از مدل Parameter برای تعیین مقادیر جایگزین شونده در قالب تعریف شده (ساختار مدل Parameter در جدول زیر ذکر شده است) |

### 3.4.1.1. مدل Parameter

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

## 3.4.2. مدل دیتای بازگشتی

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

## 3.4.3. نمونه کد

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

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](../07-sdks/README.md#جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

---

[بازگشت به فهرست مطالب](../README.md)
