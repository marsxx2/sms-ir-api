# پکیج‌های رسمی sms.ir (SDK Reference)


این فایل، مرجع خودکفای پنج پکیج رسمی sms.ir است (کپی از `docs/07-sdks/` برای استفاده‌ی مستقل این skill). منبع اصلی و به‌روز، پوشه‌ی `docs/07-sdks/` در مخزن است.


## جدول تناظر متدهای API با متدهای هر SDK

| متد API (این مستند)                                                            | Node.js                  | PHP / Laravel               | TypeScript              | .NET                           | Python                       |
| ---------------------------------------------------------------------------------| ---------------------------| ------------------------------| --------------------------| ---------------------------------| --------------------------------|
| 3.1. ارسال گروهی                                      | `SendBulk`                  | `bulkSend`                     | `sendBulk`                 | `BulkSendAsync`                    | `send_bulk_sms`                  |
| 3.2. ارسال نظیر به نظیر                       | `SendLikeToLike`            | `likeToLikeSend`               | `sendLikeToLike`           | `LikeToLikeSendAsync`              | `send_like_to_like`              |
| 3.3. حذف ارسال زمان‌بندی شده              | `deleteScheduled`           | `removeScheduledMessages`      | `deleteScheduled`          | `RemoveScheduledMessagesAsync`     | `delete_scheduled`               |
| 3.4. ارسال Verify                                   | `SendVerifyCode`            | `verifySend`                   | `sendVerifyCode`           | `VerifySendAsync`                  | `send_verify_code`               |
| 3.5. ارسال از طریق URL                        | در README مستند نشده        | در README مستند نشده           | `sendByURL`                | در README مستند نشده               | در README مستند نشده             |
| 4.1. گزارش پیامک                            | `ReportMessage`             | `getReportByMessageId`         | `reportMessage`            | `GetReportAsync`                   | `report_message`                 |
| 4.2. گزارش مجموعه ارسال‌های روز                | در README مستند نشده        | `getSendPacks`                 | `reportDailyPack`          | `GetSendPacksAsync`                | در README مستند نشده             |
| 4.3. گزارش مجموعه ارسال                        | `ReportPack`                 | `getReportByPackId`            | `reportPackById`           | `GetReportAsync` (overload)        | `report_pack`                    |
| 4.4. گزارش ارسال‌های روز                       | `ReportToday`                | `getLiveReport`                | `reportTodayLive`          | `GetLiveReportAsync`               | `report_today`                   |
| 4.5. گزارش ارسال‌های آرشیو شده              | `ReportArchived`             | `getArchivedReport`            | `reportArchive`            | `GetArchivedReportAsync`           | `report_archived`                |
| 4.6. گزارش تازه‌ترین پیامک‌های دریافتی    | `ReportLatestReceived`       | `getLatestReceives`            | `reportLatestReceive`      | `GetLatestReceivesAsync`           | `report_latest_received`         |
| 4.7. گزارش پیامک‌های دریافتی روز            | `ReportTodayReceived`        | `getLiveReceives`              | `reportReceiveLive`        | `GetLiveReceivesAsync`             | `report_today_received`          |
| 4.8. گزارش پیامک‌های دریافتی آرشیو شده   | `ReportArchivedReceived`     | `getArchivedReceives`          | `reportReceiveArchive`     | `GetArchivedReceivesAsync`         | `report_archived_received`       |
| 5.1. دریافت مقدار اعتبار فعلی                    | `getCredit`                  | `getCredit`                    | `getCredit`                | `GetCreditAsync`                   | `get_credit`                     |
| 5.2. دریافت لیست خطوط                              | `getLineNumbers`             | `getLines`                     | `getLineNumbers`           | `GetLinesAsync`                    | `get_line_numbers`               |

> ستون‌هایی که «در README مستند نشده» ذکر شده‌اند، به این معنا نیست که آن قابلیت در پکیج وجود ندارد؛ صرفاً در فایل README مخزن مربوطه، متد معادل آن به‌صراحت ذکر نشده است. برای اطمینان، به سورس‌کد پکیج یا Issues مخزن مراجعه کنید.



---


# SDK: Node.js (smsir-js)

- **مخزن:** [IPeCompany/SmsPanelV2.nodejs](https://github.com/IPeCompany/SmsPanelV2.nodejs)
- **نصب:** `npm install smsir-js`
- **لایسنس:** MIT

## نصب و راه‌اندازی

```js
const { Smsir } = require('smsir-js')
// یا در پروژه‌های ماژولار (Vue.js، React.js و ...):
// import { Smsir } from 'smsir-js'

/**
 * @param {string} api_key   کلید خصوصی وب‌سرویس (بخش برنامه‌نویسان پنل)
 * @param {int}    line_number  شماره خط پیش‌فرض برای ارسال‌ها
 */
const smsir = new Smsir(api_key, line_number)
```

## مرجع متدها

### `SendBulk(MessageText, Mobiles, SendDateTime, line_number)`

ارسال یک متن پیامک به گروهی از شماره‌موبایل‌ها — معادل 3.1. ارسال گروهی.

```js
smsir.SendBulk('سلام، این یک پیام آزمایشی است', ['09123456789'], null, line_number)
```

### `SendLikeToLike(MessageTexts, Mobiles, SendDateTime, line_number)`

ارسال چند پیامک متفاوت به چند شماره، به‌صورت نظیر به نظیر — معادل 3.2. ارسال نظیر به نظیر.

```js
smsir.SendLikeToLike(
  ['سلام علی', 'سلام سارا'],
  ['09121111111', '09122222222'],
  null,
  line_number
)
```

### `deleteScheduled(PackId)`

حذف یک بسته‌ی ارسال زمان‌بندی‌شده که هنوز ارسال نشده — معادل 3.3. حذف ارسال زمان‌بندی شده.

```js
smsir.deleteScheduled(packId)
```

### `SendVerifyCode(Mobile, TemplateId, Parameters)`

ارسال پیامک بر اساس یک قالب از پیش تعریف‌شده (کد تایید، فاکتور و ...) — معادل 3.4. ارسال Verify.

```js
smsir.SendVerifyCode('09123456789', 100000, [
  { name: 'Code', value: '12345' },
])
```

> ⚠️ این پکیج در README خود متدی برای 3.5. ارسال از طریق URL مستند نکرده است.

### `ReportMessage(MessageId)`

دریافت گزارش یک پیامک ارسال‌شده — معادل 4.1. گزارش پیامک.

```js
smsir.ReportMessage(messageId)
```

### `ReportPack(PackId)`

دریافت گزارش پیامک‌های یک مجموعه ارسال — معادل 4.3. گزارش مجموعه ارسال.

```js
smsir.ReportPack(packId)
```

### `ReportToday(pageSize, pageNumber)`

دریافت گزارش ارسال‌های امروز، با صفحه‌بندی (مقدار پیش‌فرض `pageSize`: 10) — معادل 4.4. گزارش ارسال‌های روز.

```js
smsir.ReportToday(20, 1)
```

### `ReportArchived(fromDate, toDate, pageSize, pageNumber)`

دریافت گزارش ارسال‌های آرشیو شده در یک بازه‌ی زمانی — معادل 4.5. گزارش ارسال‌های آرشیو شده.

```js
smsir.ReportArchived(fromDateUnix, toDateUnix, 100, 1)
```

### `ReportLatestReceived(count)`

دریافت تازه‌ترین پیامک‌های دریافتی — معادل 4.6. گزارش تازه‌ترین پیامک‌های دریافتی.

```js
smsir.ReportLatestReceived(50)
```

### `ReportTodayReceived(pageSize, pageNumber)`

دریافت پیامک‌های دریافتی امروز — معادل 4.7. گزارش پیامک‌های دریافتی روز.

```js
smsir.ReportTodayReceived(20, 1)
```

### `ReportArchivedReceived(fromDate, toDate, pageSize, pageNumber)`

دریافت پیامک‌های دریافتی آرشیو شده — معادل 4.8. گزارش پیامک‌های دریافتی آرشیو شده.

```js
smsir.ReportArchivedReceived(fromDateUnix, toDateUnix, 100, 1)
```

### `getCredit()`

دریافت مقدار اعتبار حساب — معادل 5.1. دریافت مقدار اعتبار فعلی. طبق آزمایش عملی، مقدار بازگشتی **تعداد پیامک باقی‌مانده** است، نه مبلغ ریالی (به یادداشت بخش ۵.۱ مراجعه کنید).

```js
const credit = await smsir.getCredit()
```

### `getLineNumbers()`

دریافت لیست خطوط فعال حساب — معادل 5.2. دریافت لیست خطوط.

```js
const lines = await smsir.getLineNumbers()
```

## پیوندهای بیشتر

- [CHANGELOG مخزن](https://github.com/IPeCompany/SmsPanelV2.nodejs/blob/master/CHANGELOG.md)
- [صفحه‌ی Issues برای گزارش باگ یا درخواست ویژگی](https://github.com/IPeCompany/SmsPanelV2.nodejs/issues)



---


# SDK: PHP / Laravel (smsir-php)

- **مخزن:** [IPeCompany/smsir-php](https://github.com/IPeCompany/smsir-php)
- **نصب:** `composer require ipe/smsir-php`
- **لایسنس:** طبق مخزن (به فایل LICENSE مراجعه کنید)

## نصب و راه‌اندازی

پس از نصب پکیج با Composer، کلید وب‌سرویس را (از بخش «برنامه‌نویسان» پنل sms.ir) در فایل `.env` پروژه‌ی Laravel خود قرار دهید:

```env
SMSIR_API_KEY=your_api_key_here
```

سپس در کد خود از Facade زیر استفاده کنید:

```php
use Ipe\Sdk\Facades\SmsIr;
```

## ویژگی‌ها

- ارسال پیامک‌های تکی و گروهی
- ارسال پیامک‌های نظیر به نظیر
- ارسال پیامک‌های تایید (Verify)
- زمان‌بندی ارسال پیامک
- گزارش‌گیری از وضعیت پیامک‌های ارسال شده
- مشاهده پیامک‌های دریافت‌شده
- دریافت اعتبار فعلی و مدیریت خطوط

## مرجع متدها

### `bulkSend($lineNumber, $messageText, $mobiles, $sendDateTime)`

ارسال پیامک گروهی — معادل 3.1. ارسال گروهی.

```php
$lineNumber = "1234567890";
$messageText = "این یک پیام آزمایشی است.";
$mobiles = ["09123456789", "09198765432"];
$sendDateTime = null; // برای ارسال آنی

$response = SmsIr::bulkSend($lineNumber, $messageText, $mobiles, $sendDateTime);
```

### `likeToLikeSend($lineNumber, $messageTexts, $mobiles, $sendDateTime)`

ارسال نظیر به نظیر (هر شماره پیام مخصوص به خود) — معادل 3.2. ارسال نظیر به نظیر.

```php
$messageTexts = ["پیام ۱ برای شماره ۱", "پیام ۲ برای شماره ۲"];
$mobiles = ["09123456789", "09198765432"];

$response = SmsIr::likeToLikeSend($lineNumber, $messageTexts, $mobiles, null);
```

### `removeScheduledMessages($packId)`

حذف یک بسته‌ی ارسال زمان‌بندی‌شده — معادل 3.3. حذف ارسال زمان‌بندی شده.

```php
$response = SmsIr::removeScheduledMessages($packId);
```

### `verifySend($mobile, $templateId, $parameters)`

ارسال پیامک بر اساس قالب از پیش تعریف‌شده — معادل 3.4. ارسال Verify.

```php
$mobile = "09120000000";
$templateId = 100000;
$parameters = [
    ["name" => "Code", "value" => "12345"],
];

$response = SmsIr::verifySend($mobile, $templateId, $parameters);
```

> ⚠️ این پکیج در README خود متدی برای 3.5. ارسال از طریق URL مستند نکرده است.

### `getReportByMessageId($messageId)`

دریافت گزارش تحویل یک پیامک — معادل 4.1. گزارش پیامک.

```php
$response = SmsIr::getReportByMessageId($messageId);
```

### `getSendPacks($pageNumber, $pageSize)`

دریافت لیست مجموعه‌های ارسال — معادل 4.2. گزارش مجموعه ارسال‌های روز.

```php
$response = SmsIr::getSendPacks(1, 100);
```

### `getReportByPackId($packId)`

دریافت گزارش پیامک‌های یک مجموعه‌ی ارسال خاص — معادل 4.3. گزارش مجموعه ارسال.

```php
$response = SmsIr::getReportByPackId($packId);
```

### `getLiveReport($pageNumber, $pageSize, $sortByNewest)`

گزارش زنده‌ی پیامک‌های ارسال‌شده در روز جاری — معادل 4.4. گزارش ارسال‌های روز.

```php
$response = SmsIr::getLiveReport(1, 100, true);
```

### `getArchivedReport($pageNumber, $pageSize, $fromDate, $toDate, $sortByNewest)`

گزارش آرشیو شده‌ی ارسال‌ها در یک بازه‌ی زمانی — معادل 4.5. گزارش ارسال‌های آرشیو شده.

```php
$response = SmsIr::getArchivedReport(1, 100, 1609459200, 1612137600, true);
```

### `getLatestReceives($count = 100)`

دریافت آخرین پیام‌های دریافتی — معادل 4.6. گزارش تازه‌ترین پیامک‌های دریافتی.

```php
$response = SmsIr::getLatestReceives(50);
```

### `getLiveReceives($pageNumber, $pageSize, $sortByNewest)`

دریافت پیام‌های دریافتی امروز، با صفحه‌بندی و مرتب‌سازی — معادل 4.7. گزارش پیامک‌های دریافتی روز.

```php
$response = SmsIr::getLiveReceives(2, 50, true);
```

### `getArchivedReceives($pageNumber, $pageSize, $fromDate, $toDate)`

دریافت پیام‌های دریافتی آرشیو شده در یک بازه‌ی زمانی — معادل 4.8. گزارش پیامک‌های دریافتی آرشیو شده.

```php
$fromDate = 1672531200; // 2023-01-01 00:00:00 UTC
$toDate   = 1704067199; // 2023-12-31 23:59:59 UTC
$response = SmsIr::getArchivedReceives(1, 50, $fromDate, $toDate);
```

### `getCredit()`

دریافت مقدار اعتبار حساب — معادل 5.1. دریافت مقدار اعتبار فعلی. طبق آزمایش عملی، مقدار بازگشتی **تعداد پیامک باقی‌مانده** است، نه مبلغ ریالی (به یادداشت بخش ۵.۱ مراجعه کنید).

```php
$response = SmsIr::getCredit();
```

### `getLines()`

دریافت لیست خطوط پیامکی فعال — معادل 5.2. دریافت لیست خطوط.

```php
$response = SmsIr::getLines();
```

## پیوندهای بیشتر

- [صفحه‌ی Issues برای گزارش باگ یا درخواست ویژگی](https://github.com/IPeCompany/smsir-php/issues)



---


# SDK: TypeScript (sms-typescript)

- **مخزن:** [IPeCompany/SmsPanelV2.TypeScript](https://github.com/IPeCompany/SmsPanelV2.TypeScript)
- **نصب:** `npm install sms-typescript`
- **لایسنس:** MIT
- **پیش‌نیاز:** Node.js ≥ 18 (به دلیل استفاده از `fetch` نیتیو)، TypeScript ≥ 4.5 در صورت استفاده از TS

این پکیج جدیدترین و کامل‌ترین SDK رسمی sms.ir است: تایپ‌های کامل TypeScript، پشتیبانی از CommonJS و ES Modules، دو API طراحی (کلاس‌محور و تابع‌محور)، و سازگاری کامل با نسخه‌ی قبلی (v1.x).

## نصب و راه‌اندازی

### API کلاس‌محور (مناسب برای برنامه‌نویسی شیءگرا)

```ts
import { Smsir } from "sms-typescript";

const sms = new Smsir("your-api-key", lineNumber);
```

### API تابع‌محور (مناسب برای برنامه‌نویسی تابعی)

```ts
import { smsBuilder } from "sms-typescript";

const sms = smsBuilder({
  apiKey: "your-api-key",
  lineNumber: lineNumber,
});
```

> API تابع‌محور شامل متدهای منسوخ‌شده (deprecated) نسخه‌ی v1.x نیست.

### CommonJS (Node.js)

```js
const { Smsir } = require("sms-typescript");
const sms = new Smsir("your-api-key", lineNumber);
```

## مرجع متدها

### `sendBulk(messageText, mobiles, sendDateTime?, customLineNumber?)`

ارسال پیامک گروهی — معادل 3.1. ارسال گروهی.

```ts
const result = await sms.sendBulk(
  "سلام دنیا!",
  ["09123456789", "09987654321"],
  Date.now() + 3600000, // اختیاری: زمان‌بندی برای یک ساعت بعد
  lineNumber              // اختیاری: خط دیگری غیر از خط پیش‌فرض
);
console.log("Pack ID:", result.data.packId);
```

### `sendLikeToLike(messageTexts, mobiles, sendDateTime?, customLineNumber?)`

ارسال نظیر به نظیر — معادل 3.2. ارسال نظیر به نظیر.

```ts
await sms.sendLikeToLike(
  ["سلام علی", "سلام سارا"],
  ["09121111111", "09122222222"]
);
```

### `deleteScheduled(packId)`

حذف یک بسته‌ی ارسال زمان‌بندی‌شده — معادل 3.3. حذف ارسال زمان‌بندی شده.

```ts
await sms.deleteScheduled("pack-id-here");
```

### `sendVerifyCode(mobile, templateId, parameters)`

ارسال پیامک بر اساس قالب از پیش تعریف‌شده — معادل 3.4. ارسال Verify.

```ts
await sms.sendVerifyCode("09123456789", templateId, [
  { name: "Code", value: "123456" },
]);
```

### `sendByURL(username, mobile, text, customLine?)`

ارسال با متد URL (روش قدیمی‌تر، برای سازگاری با گذشته) — معادل 3.5. ارسال از طریق URL.

```ts
await sms.sendByURL("username", "09123456789", "سلام دنیا!");
```

### `reportMessage(messageId)`

وضعیت تحویل یک پیامک خاص — معادل 4.1. گزارش پیامک.

```ts
const report = await sms.reportMessage("876240022");
console.log("Delivery State:", report.data.deliveryState);
```

### `reportDailyPack(pageNumber, pageSize)`

آمار مجموعه‌های ارسال روز جاری با صفحه‌بندی — معادل 4.2. گزارش مجموعه ارسال‌های روز.

```ts
const dailyPack = await sms.reportDailyPack(1, 10);
```

### `reportPackById(packId)`

تمام پیامک‌های یک مجموعه‌ی ارسال خاص — معادل 4.3. گزارش مجموعه ارسال.

```ts
const pack = await sms.reportPackById("pack-id");
```

### `reportTodayLive(pageNumber, pageSize)`

پیامک‌های ارسال‌شده‌ی امروز — معادل 4.4. گزارش ارسال‌های روز.

```ts
const today = await sms.reportTodayLive(1, 10);
```

### `reportArchive(fromDate, toDate, pageNumber, pageSize)`

پیامک‌های ارسال‌شده‌ی آرشیو شده در یک بازه‌ی زمانی — معادل 4.5. گزارش ارسال‌های آرشیو شده.

```ts
const archived = await sms.reportArchive(
  Date.now() - 86400000, // دیروز
  Date.now(),
  1,
  10
);
```

### `reportLatestReceive(count)`

آخرین پیامک‌های دریافتی — معادل 4.6. گزارش تازه‌ترین پیامک‌های دریافتی.

```ts
const received = await sms.reportLatestReceive(100);
```

### `reportReceiveLive(pageNumber, pageSize, sortByNewest)`

پیامک‌های دریافتی امروز — معادل 4.7. گزارش پیامک‌های دریافتی روز.

```ts
const live = await sms.reportReceiveLive(1, 10, true);
```

### `reportReceiveArchive(fromDate, toDate, pageNumber, pageSize)`

پیامک‌های دریافتی آرشیو شده — معادل 4.8. گزارش پیامک‌های دریافتی آرشیو شده.

```ts
const archivedReceived = await sms.reportReceiveArchive(
  Date.now() - 86400000,
  Date.now(),
  1,
  10
);
```

### `getCredit()`

دریافت مقدار اعتبار حساب — معادل 5.1. دریافت مقدار اعتبار فعلی. طبق آزمایش عملی، مقدار بازگشتی **تعداد پیامک باقی‌مانده** است، نه مبلغ ریالی (به یادداشت بخش ۵.۱ مراجعه کنید).

```ts
const credit = await sms.getCredit();
```

### `getLineNumbers()`

دریافت لیست خطوط فعال حساب — معادل 5.2. دریافت لیست خطوط.

```ts
const lines = await sms.getLineNumbers();
```

## سازگاری با نسخه‌ی v1.x

متدهای قدیمی (PascalCase مانند `SendBulk`, `SendVerifyCode`, ...) هنوز در API کلاس‌محور کار می‌کنند اما **منسوخ (deprecated)** هستند و طبق برنامه‌ی نگهدارنده‌ها در نسخه‌ی v3.0.0 حذف خواهند شد. توصیه می‌شود از متدهای جدید camelCase استفاده کنید.

## مدیریت خطا

```ts
try {
  const result = await sms.sendBulk("سلام", ["09123456789"]);
  console.log("موفق:", result.data);
} catch (error) {
  console.error("خطا:", error.message);
}
```

## پیوندهای بیشتر

- [مثال‌های تکمیلی (Angular، React، Vue.js)](https://github.com/IPeCompany/SmsPanelV2.TypeScript/blob/main/USAGE_EXAMPLES.md)
- [صفحه‌ی Issues برای گزارش باگ یا درخواست ویژگی](https://github.com/IPeCompany/SmsPanelV2.TypeScript/issues)



---


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

ارسال پیامک گروهی — معادل 3.1. ارسال گروهی.

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

ارسال نظیر به نظیر — معادل 3.2. ارسال نظیر به نظیر.

```csharp
long lineNumber = 95007079000006;
string[] messageTexts = { "Message Text 1\nSMS.ir", "Message Text 2\nSMS.ir" };
string[] mobiles = { "9120000000", "9120000001" };

var response = await smsIr.LikeToLikeSendAsync(lineNumber, messageTexts, mobiles, null);
```

### `RemoveScheduledMessagesAsync(packId)`

حذف یک بسته‌ی ارسال زمان‌بندی‌شده — معادل 3.3. حذف ارسال زمان‌بندی شده.

```csharp
Guid packId = new Guid("86D96B0E-FD89-4C19-B303-C0B4D3874063");
var response = await smsIr.RemoveScheduledMessagesAsync(packId);

RemoveScheduledMessagesResult result = response.Data;
decimal returnedCreditCount = result.ReturnedCreditCount;
decimal smsCount = result.SmsCount;
```

### `VerifySendAsync(mobile, templateId, verifySendParameters)`

ارسال پیامک بر اساس قالب از پیش تعریف‌شده — معادل 3.4. ارسال Verify.

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

> ⚠️ این پکیج در README خود متدی برای 3.5. ارسال از طریق URL مستند نکرده است.

### `GetReportAsync(messageId)`

گزارش تحویل یک پیامک خاص — معادل 4.1. گزارش پیامک.

```csharp
int messageId = 10000000;
var response = await smsIr.GetReportAsync(messageId);

MessageReportResult messageReport = response.Data;
byte? deliveryState = messageReport.DeliveryState;
decimal cost = messageReport.Cost;
```

### `GetSendPacksAsync(pageNumber, pageSize)`

لیست مجموعه‌های ارسال — معادل 4.2. گزارش مجموعه ارسال‌های روز.

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

گزارش پیامک‌های یک مجموعه‌ی ارسال خاص — معادل 4.3. گزارش مجموعه ارسال.

```csharp
Guid packId = new Guid("86D96B0E-FD89-4C19-B303-C0B4D3874063");
var response = await smsIr.GetReportAsync(packId);

MessageReportResult[] messages = response.Data;
```

### `GetLiveReportAsync(pageNumber, pageSize)`

گزارش ارسال‌های امروز — معادل 4.4. گزارش ارسال‌های روز.

```csharp
var response = await smsIr.GetLiveReportAsync(pageNumber: 1, pageSize: 100); // حداکثر 100
```

### `GetArchivedReportAsync(pageNumber, pageSize, fromDate, toDate)`

گزارش ارسال‌های آرشیو شده — معادل 4.5. گزارش ارسال‌های آرشیو شده.

```csharp
int? fromDateUnixTime = 1700598600;
int? toDateUnixTime = 1703190600;
var response = await smsIr.GetArchivedReportAsync(1, 100, fromDateUnixTime, toDateUnixTime);
```

### `GetLatestReceivesAsync(count)`

آخرین پیامک‌های دریافتی — معادل 4.6. گزارش تازه‌ترین پیامک‌های دریافتی.

```csharp
var response = await smsIr.GetLatestReceivesAsync(count: 100); // حداکثر 100
```

### `GetLiveReceivesAsync(pageNumber, pageSize)`

پیامک‌های دریافتی امروز — معادل 4.7. گزارش پیامک‌های دریافتی روز.

```csharp
var response = await smsIr.GetLiveReceivesAsync(pageNumber: 1, pageSize: 100);
```

### `GetArchivedReceivesAsync(pageNumber, pageSize, fromDate, toDate)`

پیامک‌های دریافتی آرشیو شده — معادل 4.8. گزارش پیامک‌های دریافتی آرشیو شده.

```csharp
var response = await smsIr.GetArchivedReceivesAsync(1, 100, fromDateUnixTime, toDateUnixTime);
```

### `GetCreditAsync()`

دریافت مقدار اعتبار حساب — معادل 5.1. دریافت مقدار اعتبار فعلی. طبق آزمایش عملی، مقدار بازگشتی **تعداد پیامک باقی‌مانده** است، نه مبلغ ریالی (به یادداشت بخش ۵.۱ مراجعه کنید).

```csharp
var response = await smsIr.GetCreditAsync();
decimal credit = response.Data;
```

### `GetLinesAsync()`

دریافت لیست خطوط پیامکی فعال — معادل 5.2. دریافت لیست خطوط.

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


# SDK: Python (smsir-python)

- **مخزن:** [IPeCompany/SmsPanelV2.Python](https://github.com/IPeCompany/SmsPanelV2.Python)
- **نصب:** `pip install smsir-python`
- **لایسنس:** MIT
- **پیش‌نیاز:** پکیج `requests`

## نصب و راه‌اندازی

```bash
pip install smsir-python
```

```python
from sms_ir import SmsIr

sms_ir = SmsIr(
    api_key,
    linenumber,
)
```

## مرجع متدها

### `send_sms(number, message, linenumber)`

ارسال پیامک به یک شماره‌ی مشخص.

```python
sms_ir.send_sms(number, message, linenumber)
```

### `send_bulk_sms(numbers, message, linenumber)`

ارسال یک متن به چند شماره‌موبایل — معادل 3.1. ارسال گروهی.

```python
sms_ir.send_bulk_sms(numbers, message, linenumber)
```

### `send_like_to_like(numbers, messages, linenumber, send_date_time)`

ارسال نظیر به نظیر — معادل 3.2. ارسال نظیر به نظیر.

```python
sms_ir.send_like_to_like(numbers, messages, linenumber, send_date_time)
```

### `delete_scheduled(pack_id)`

حذف یک بسته‌ی ارسال زمان‌بندی‌شده — معادل 3.3. حذف ارسال زمان‌بندی شده.

```python
sms_ir.delete_scheduled(pack_id)
```

### `send_verify_code(number, template_id, parameters)`

ارسال پیامک بر اساس قالب از پیش تعریف‌شده — معادل 3.4. ارسال Verify.

```python
sms_ir.send_verify_code(
    number="+989111111111",
    template_id=10000,
    parameters=[
        {"name": "code", "value": 12345},
    ],
)
```

> ⚠️ این پکیج در README خود متدی برای 3.5. ارسال از طریق URL مستند نکرده است.

### `report_message(message_id)`

گزارش یک پیامک ارسال‌شده — معادل 4.1. گزارش پیامک.

```python
sms_ir.report_message(message_id)
```

> ⚠️ این پکیج در README خود متد مجزایی برای 4.2. گزارش مجموعه ارسال‌های روز (لیست پک‌ها) مستند نکرده است.

### `report_pack(pack_id)`

گزارش یک مجموعه‌ی ارسال — معادل 4.3. گزارش مجموعه ارسال.

```python
sms_ir.report_pack(pack_id)
```

### `report_today(page_size, page_number)`

گزارش ارسال‌های امروز — معادل 4.4. گزارش ارسال‌های روز.

```python
sms_ir.report_today(page_size, page_number)
```

### `report_archived(from_date, to_date, page_size, page_number)`

گزارش ارسال‌های آرشیو شده — معادل 4.5. گزارش ارسال‌های آرشیو شده.

```python
sms_ir.report_archived(from_date, to_date, page_size, page_number)
```

### `report_latest_received(count)`

آخرین پیامک‌های دریافتی — معادل 4.6. گزارش تازه‌ترین پیامک‌های دریافتی.

```python
sms_ir.report_latest_received(count)
```

### `report_today_received(page_size, page_number)`

پیامک‌های دریافتی امروز — معادل 4.7. گزارش پیامک‌های دریافتی روز.

```python
sms_ir.report_today_received(page_size, page_number)
```

### `report_archived_received(from_date, to_date, page_size, page_number)`

پیامک‌های دریافتی آرشیو شده — معادل 4.8. گزارش پیامک‌های دریافتی آرشیو شده.

```python
sms_ir.report_archived_received(from_date, to_date, page_size, page_number)
```

### `get_credit()`

دریافت مقدار اعتبار حساب — معادل 5.1. دریافت مقدار اعتبار فعلی. طبق آزمایش عملی، مقدار بازگشتی **تعداد پیامک باقی‌مانده** است، نه مبلغ ریالی (به یادداشت بخش ۵.۱ مراجعه کنید).

```python
sms_ir.get_credit()
```

### `get_line_numbers()`

دریافت لیست خطوط فعال — معادل 5.2. دریافت لیست خطوط.

```python
sms_ir.get_line_numbers()
```

## پیوندهای بیشتر

- [صفحه‌ی Issues برای گزارش باگ یا درخواست ویژگی](https://github.com/IPeCompany/SmsPanelV2.Python/issues)
- [پکیج در PyPI](https://pypi.org/project/smsir-python/)


