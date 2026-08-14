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

ارسال پیامک گروهی — معادل [3.1. ارسال گروهی](../03-sends/01-bulk.md).

```php
$lineNumber = "1234567890";
$messageText = "این یک پیام آزمایشی است.";
$mobiles = ["09123456789", "09198765432"];
$sendDateTime = null; // برای ارسال آنی

$response = SmsIr::bulkSend($lineNumber, $messageText, $mobiles, $sendDateTime);
```

### `likeToLikeSend($lineNumber, $messageTexts, $mobiles, $sendDateTime)`

ارسال نظیر به نظیر (هر شماره پیام مخصوص به خود) — معادل [3.2. ارسال نظیر به نظیر](../03-sends/02-like-to-like.md).

```php
$messageTexts = ["پیام ۱ برای شماره ۱", "پیام ۲ برای شماره ۲"];
$mobiles = ["09123456789", "09198765432"];

$response = SmsIr::likeToLikeSend($lineNumber, $messageTexts, $mobiles, null);
```

### `removeScheduledMessages($packId)`

حذف یک بسته‌ی ارسال زمان‌بندی‌شده — معادل [3.3. حذف ارسال زمان‌بندی شده](../03-sends/03-delete-scheduled.md).

```php
$response = SmsIr::removeScheduledMessages($packId);
```

### `verifySend($mobile, $templateId, $parameters)`

ارسال پیامک بر اساس قالب از پیش تعریف‌شده — معادل [3.4. ارسال Verify](../03-sends/04-verify.md).

```php
$mobile = "09120000000";
$templateId = 100000;
$parameters = [
    ["name" => "Code", "value" => "12345"],
];

$response = SmsIr::verifySend($mobile, $templateId, $parameters);
```

> ⚠️ این پکیج در README خود متدی برای [3.5. ارسال از طریق URL](../03-sends/05-send-via-url.md) مستند نکرده است.

### `getReportByMessageId($messageId)`

دریافت گزارش تحویل یک پیامک — معادل [4.1. گزارش پیامک](../04-reports/01-send-reports.md).

```php
$response = SmsIr::getReportByMessageId($messageId);
```

### `getSendPacks($pageNumber, $pageSize)`

دریافت لیست مجموعه‌های ارسال — معادل [4.2. گزارش مجموعه ارسال‌های روز](../04-reports/02-live-pack.md).

```php
$response = SmsIr::getSendPacks(1, 100);
```

### `getReportByPackId($packId)`

دریافت گزارش پیامک‌های یک مجموعه‌ی ارسال خاص — معادل [4.3. گزارش مجموعه ارسال](../04-reports/03-send-pack.md).

```php
$response = SmsIr::getReportByPackId($packId);
```

### `getLiveReport($pageNumber, $pageSize, $sortByNewest)`

گزارش زنده‌ی پیامک‌های ارسال‌شده در روز جاری — معادل [4.4. گزارش ارسال‌های روز](../04-reports/04-send-live.md).

```php
$response = SmsIr::getLiveReport(1, 100, true);
```

### `getArchivedReport($pageNumber, $pageSize, $fromDate, $toDate, $sortByNewest)`

گزارش آرشیو شده‌ی ارسال‌ها در یک بازه‌ی زمانی — معادل [4.5. گزارش ارسال‌های آرشیو شده](../04-reports/05-send-archive.md).

```php
$response = SmsIr::getArchivedReport(1, 100, 1609459200, 1612137600, true);
```

### `getLatestReceives($count = 100)`

دریافت آخرین پیام‌های دریافتی — معادل [4.6. گزارش تازه‌ترین پیامک‌های دریافتی](../04-reports/06-receive-latest.md).

```php
$response = SmsIr::getLatestReceives(50);
```

### `getLiveReceives($pageNumber, $pageSize, $sortByNewest)`

دریافت پیام‌های دریافتی امروز، با صفحه‌بندی و مرتب‌سازی — معادل [4.7. گزارش پیامک‌های دریافتی روز](../04-reports/07-receive-live.md).

```php
$response = SmsIr::getLiveReceives(2, 50, true);
```

### `getArchivedReceives($pageNumber, $pageSize, $fromDate, $toDate)`

دریافت پیام‌های دریافتی آرشیو شده در یک بازه‌ی زمانی — معادل [4.8. گزارش پیامک‌های دریافتی آرشیو شده](../04-reports/08-receive-archive.md).

```php
$fromDate = 1672531200; // 2023-01-01 00:00:00 UTC
$toDate   = 1704067199; // 2023-12-31 23:59:59 UTC
$response = SmsIr::getArchivedReceives(1, 50, $fromDate, $toDate);
```

### `getCredit()`

دریافت مقدار اعتبار حساب — معادل [5.1. دریافت مقدار اعتبار فعلی](../05-settings/01-credit.md). طبق آزمایش عملی، مقدار بازگشتی **تعداد پیامک باقی‌مانده** است، نه مبلغ ریالی (به یادداشت بخش ۵.۱ مراجعه کنید).

```php
$response = SmsIr::getCredit();
```

### `getLines()`

دریافت لیست خطوط پیامکی فعال — معادل [5.2. دریافت لیست خطوط](../05-settings/02-line.md).

```php
$response = SmsIr::getLines();
```

## پیوندهای بیشتر

- [صفحه‌ی Issues برای گزارش باگ یا درخواست ویژگی](https://github.com/IPeCompany/smsir-php/issues)

---

[بازگشت به فهرست SDKها](README.md) · [بازگشت به فهرست مطالب](../README.md)
