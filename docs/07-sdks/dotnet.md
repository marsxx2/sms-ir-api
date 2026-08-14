# SDK: .NET (IPE.SmsIr)

- **مخزن:** [IPeCompany/SmsPanelV2.dotNet](https://github.com/IPeCompany/SmsPanelV2.dotNet)
- **نصب:** `dotnet add package IPE.SmsIR` (یا از طریق NuGet Package Manager در Visual Studio)
- **نمونه‌ی کامل:** [پروژه‌ی نمونه ASP.NET Core](https://github.com/IPeCompany/SmsPanelV2.DotNetCore.Samples)

## نصب و راه‌اندازی

```bash
dotnet add package IPE.SmsIR
```

یا در Visual Studio از طریق Package Manager Console:

```powershell
Install-Package IPE.SmsIR
```

## شروع سریع

```csharp
SmsIr smsIr = new SmsIr("YOUR API KEY");

var bulkSendResult = await smsIr.BulkSendAsync(
    lineNumber, "متن پیام شما", new string[] { "9120000000" });

var verificationSendResult = await smsIr.VerifySendAsync(
    "9120000000", templateId, new VerifySendParameter[] {
        new VerifySendParameter("Code", "12345")
    });
```

## مرجع متدها

### `BulkSendAsync(lineNumber, messageText, mobiles, sendDateTime)`

ارسال پیامک گروهی — معادل [3.1. ارسال گروهی](../03-sends/01-bulk.md).

```csharp
SmsIr smsIr = new SmsIr("YOUR API KEY");

long lineNumber = 95007079000006;
string messageText = "Message Text\nSMS.ir";
string[] mobiles = { "9120000000", "9120000001" };
int? sendDateTime = null; // یونیکس‌تایم، مثلا: 1704094200

var response = await smsIr.BulkSendAsync(lineNumber, messageText, mobiles, sendDateTime);

SendResult sendResult = response.Data;
Guid packId = sendResult.PackId;
int?[] messageIds = sendResult.MessageIds;
decimal cost = sendResult.Cost;
```

### `LikeToLikeSendAsync(lineNumber, messageTexts, mobiles, sendDateTime)`

ارسال نظیر به نظیر — معادل [3.2. ارسال نظیر به نظیر](../03-sends/02-like-to-like.md).

```csharp
long lineNumber = 95007079000006;
string[] messageTexts = { "Message Text 1\nSMS.ir", "Message Text 2\nSMS.ir" };
string[] mobiles = { "9120000000", "9120000001" };

var response = await smsIr.LikeToLikeSendAsync(lineNumber, messageTexts, mobiles, null);
```

### `RemoveScheduledMessagesAsync(packId)`

حذف یک بسته‌ی ارسال زمان‌بندی‌شده — معادل [3.3. حذف ارسال زمان‌بندی شده](../03-sends/03-delete-scheduled.md).

```csharp
Guid packId = new Guid("86D96B0E-FD89-4C19-B303-C0B4D3874063");
var response = await smsIr.RemoveScheduledMessagesAsync(packId);

RemoveScheduledMessagesResult result = response.Data;
decimal returnedCreditCount = result.ReturnedCreditCount;
decimal smsCount = result.SmsCount;
```

### `VerifySendAsync(mobile, templateId, verifySendParameters)`

ارسال پیامک بر اساس قالب از پیش تعریف‌شده — معادل [3.4. ارسال Verify](../03-sends/04-verify.md).

```csharp
string mobile = "9120000000";
int templateId = 200000;
VerifySendParameter[] verifySendParameters = {
    new VerifySendParameter("NAME", "User Name"),
    new VerifySendParameter("CODE", "12345"),
};

var response = await smsIr.VerifySendAsync(mobile, templateId, verifySendParameters);

VerifySendResult sendResult = response.Data;
int messageId = sendResult.MessageId;
decimal cost = sendResult.Cost;
```

> ⚠️ این پکیج در README خود متدی برای [3.5. ارسال از طریق URL](../03-sends/05-send-via-url.md) مستند نکرده است.

### `GetReportAsync(messageId)`

گزارش تحویل یک پیامک خاص — معادل [4.1. گزارش پیامک](../04-reports/01-send-reports.md).

```csharp
int messageId = 10000000;
var response = await smsIr.GetReportAsync(messageId);

MessageReportResult messageReport = response.Data;
byte? deliveryState = messageReport.DeliveryState;
decimal cost = messageReport.Cost;
```

### `GetSendPacksAsync(pageNumber, pageSize)`

لیست مجموعه‌های ارسال — معادل [4.2. گزارش مجموعه ارسال‌های روز](../04-reports/02-live-pack.md).

```csharp
var response = await smsIr.GetSendPacksAsync(pageNumber: 1, pageSize: 100);

PackResult[] packs = response.Data;
foreach (var pack in packs)
{
    Guid packId = pack.PackId;
    long recipientCount = pack.RecipientCount;
}
```

### `GetReportAsync(packId)` (overload)

گزارش پیامک‌های یک مجموعه‌ی ارسال خاص — معادل [4.3. گزارش مجموعه ارسال](../04-reports/03-send-pack.md).

```csharp
Guid packId = new Guid("86D96B0E-FD89-4C19-B303-C0B4D3874063");
var response = await smsIr.GetReportAsync(packId);

MessageReportResult[] messages = response.Data;
```

### `GetLiveReportAsync(pageNumber, pageSize)`

گزارش ارسال‌های امروز — معادل [4.4. گزارش ارسال‌های روز](../04-reports/04-send-live.md).

```csharp
var response = await smsIr.GetLiveReportAsync(pageNumber: 1, pageSize: 100); // حداکثر 100
```

### `GetArchivedReportAsync(pageNumber, pageSize, fromDate, toDate)`

گزارش ارسال‌های آرشیو شده — معادل [4.5. گزارش ارسال‌های آرشیو شده](../04-reports/05-send-archive.md).

```csharp
int? fromDateUnixTime = 1700598600;
int? toDateUnixTime = 1703190600;
var response = await smsIr.GetArchivedReportAsync(1, 100, fromDateUnixTime, toDateUnixTime);
```

### `GetLatestReceivesAsync(count)`

آخرین پیامک‌های دریافتی — معادل [4.6. گزارش تازه‌ترین پیامک‌های دریافتی](../04-reports/06-receive-latest.md).

```csharp
var response = await smsIr.GetLatestReceivesAsync(count: 100); // حداکثر 100
```

### `GetLiveReceivesAsync(pageNumber, pageSize)`

پیامک‌های دریافتی امروز — معادل [4.7. گزارش پیامک‌های دریافتی روز](../04-reports/07-receive-live.md).

```csharp
var response = await smsIr.GetLiveReceivesAsync(pageNumber: 1, pageSize: 100);
```

### `GetArchivedReceivesAsync(pageNumber, pageSize, fromDate, toDate)`

پیامک‌های دریافتی آرشیو شده — معادل [4.8. گزارش پیامک‌های دریافتی آرشیو شده](../04-reports/08-receive-archive.md).

```csharp
var response = await smsIr.GetArchivedReceivesAsync(1, 100, fromDateUnixTime, toDateUnixTime);
```

### `GetCreditAsync()`

دریافت مقدار اعتبار حساب — معادل [5.1. دریافت مقدار اعتبار فعلی](../05-settings/01-credit.md). طبق آزمایش عملی، مقدار بازگشتی **تعداد پیامک باقی‌مانده** است، نه مبلغ ریالی (به یادداشت بخش ۵.۱ مراجعه کنید).

```csharp
var response = await smsIr.GetCreditAsync();
decimal credit = response.Data;
```

### `GetLinesAsync()`

دریافت لیست خطوط پیامکی فعال — معادل [5.2. دریافت لیست خطوط](../05-settings/02-line.md).

```csharp
var response = await smsIr.GetLinesAsync();
long[] lines = response.Data;
```

## مدیریت خطا

```csharp
try
{
    var response = await smsIr.VerifySendAsync(mobile, templateId, verifySendParameters);
}
catch (Exception ex)
{
    // برای جزئیات بیشتر کدهای وضعیت: https://app.sms.ir/developer/help/statusCode
    string errorName = ex.GetType().Name;
    string description = errorName switch
    {
        "UnauthorizedException" => "کلید API نامعتبر است یا دسترسی رد شده.",
        "LogicalException" => "پارامترهای درخواست را بررسی و اصلاح کنید.",
        "TooManyRequestException" => "تعداد درخواست‌ها از حد مجاز عبور کرده است.",
        "UnexpectedException" or "InvalidOperationException" => "خطای غیرمنتظره در سرور رخ داده است.",
        _ => "ارسال درخواست به دلیل خطای نامشخص ممکن نشد.",
    };
}
```

## پیوندهای بیشتر

- [صفحه‌ی Issues برای گزارش باگ یا درخواست ویژگی](https://github.com/IPeCompany/SmsPanelV2.dotNet/issues)
- [پکیج در NuGet](https://www.nuget.org/packages/IPE.SmsIr)

---

[بازگشت به فهرست SDKها](README.md) · [بازگشت به فهرست مطالب](../README.md)
