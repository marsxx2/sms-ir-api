# 7. کتابخانه‌های رسمی (SDK)

علاوه بر فراخوانی مستقیم REST API، تیم sms.ir کتابخانه‌های رسمی (SDK) برای چند زبان و فریم‌ورک پرکاربرد منتشر کرده که همان متدهای این مستند را به‌صورت آماده و تایپ‌شده در اختیار قرار می‌دهند. فهرست این پکیج‌ها در صفحه [پکیج‌های وب سرویس](https://sms.ir/web-service/پکیج-های-وب-سرویس/) سایت sms.ir نیز آمده است.

> در تمام پکیج‌ها، کلید API همان کلیدی است که طبق [بخش ۱.۵](../01-introduction.md) از پنل برنامه‌نویسان دریافت می‌کنید.

## فهرست پکیج‌ها

| زبان / فریم‌ورک | مخزن گیت‌هاب                                                                | نصب                               | مستند کامل                          |
| ----------------- | ------------------------------------------------------------------------------ | ----------------------------------- | -------------------------------------- |
| Node.js            | [SmsPanelV2.nodejs](https://github.com/IPeCompany/SmsPanelV2.nodejs)           | `npm install smsir-js`              | [nodejs.md](nodejs.md)                 |
| PHP / Laravel      | [smsir-php](https://github.com/IPeCompany/smsir-php)                           | `composer require ipe/smsir-php`    | [php.md](php.md)                       |
| TypeScript         | [SmsPanelV2.TypeScript](https://github.com/IPeCompany/SmsPanelV2.TypeScript)   | `npm install sms-typescript`        | [typescript.md](typescript.md)         |
| .NET               | [SmsPanelV2.dotNet](https://github.com/IPeCompany/SmsPanelV2.dotNet)           | `dotnet add package IPE.SmsIR`      | [dotnet.md](dotnet.md)                 |
| Python             | [SmsPanelV2.Python](https://github.com/IPeCompany/SmsPanelV2.Python)           | `pip install smsir-python`          | [python.md](python.md)                 |

## جدول تناظر متدهای API با متدهای هر SDK

| متد API (این مستند)                                                            | Node.js                  | PHP / Laravel               | TypeScript              | .NET                           | Python                       |
| ---------------------------------------------------------------------------------| ---------------------------| ------------------------------| --------------------------| ---------------------------------| --------------------------------|
| [3.1. ارسال گروهی](../03-sends/01-bulk.md)                                      | `SendBulk`                  | `bulkSend`                     | `sendBulk`                 | `BulkSendAsync`                    | `send_bulk_sms`                  |
| [3.2. ارسال نظیر به نظیر](../03-sends/02-like-to-like.md)                       | `SendLikeToLike`            | `likeToLikeSend`               | `sendLikeToLike`           | `LikeToLikeSendAsync`              | `send_like_to_like`              |
| [3.3. حذف ارسال زمان‌بندی شده](../03-sends/03-delete-scheduled.md)              | `deleteScheduled`           | `removeScheduledMessages`      | `deleteScheduled`          | `RemoveScheduledMessagesAsync`     | `delete_scheduled`               |
| [3.4. ارسال Verify](../03-sends/04-verify.md)                                   | `SendVerifyCode`            | `verifySend`                   | `sendVerifyCode`           | `VerifySendAsync`                  | `send_verify_code`               |
| [3.5. ارسال از طریق URL](../03-sends/05-send-via-url.md)                        | در README مستند نشده        | در README مستند نشده           | `sendByURL`                | در README مستند نشده               | در README مستند نشده             |
| [4.1. گزارش پیامک](../04-reports/01-send-reports.md)                            | `ReportMessage`             | `getReportByMessageId`         | `reportMessage`            | `GetReportAsync`                   | `report_message`                 |
| [4.2. گزارش مجموعه ارسال‌های روز](../04-reports/02-live-pack.md)                | در README مستند نشده        | `getSendPacks`                 | `reportDailyPack`          | `GetSendPacksAsync`                | در README مستند نشده             |
| [4.3. گزارش مجموعه ارسال](../04-reports/03-send-pack.md)                        | `ReportPack`                 | `getReportByPackId`            | `reportPackById`           | `GetReportAsync` (overload)        | `report_pack`                    |
| [4.4. گزارش ارسال‌های روز](../04-reports/04-send-live.md)                       | `ReportToday`                | `getLiveReport`                | `reportTodayLive`          | `GetLiveReportAsync`               | `report_today`                   |
| [4.5. گزارش ارسال‌های آرشیو شده](../04-reports/05-send-archive.md)              | `ReportArchived`             | `getArchivedReport`            | `reportArchive`            | `GetArchivedReportAsync`           | `report_archived`                |
| [4.6. گزارش تازه‌ترین پیامک‌های دریافتی](../04-reports/06-receive-latest.md)    | `ReportLatestReceived`       | `getLatestReceives`            | `reportLatestReceive`      | `GetLatestReceivesAsync`           | `report_latest_received`         |
| [4.7. گزارش پیامک‌های دریافتی روز](../04-reports/07-receive-live.md)            | `ReportTodayReceived`        | `getLiveReceives`              | `reportReceiveLive`        | `GetLiveReceivesAsync`             | `report_today_received`          |
| [4.8. گزارش پیامک‌های دریافتی آرشیو شده](../04-reports/08-receive-archive.md)   | `ReportArchivedReceived`     | `getArchivedReceives`          | `reportReceiveArchive`     | `GetArchivedReceivesAsync`         | `report_archived_received`       |
| [5.1. دریافت مقدار اعتبار فعلی](../05-settings/01-credit.md)                    | `getCredit`                  | `getCredit`                    | `getCredit`                | `GetCreditAsync`                   | `get_credit`                     |
| [5.2. دریافت لیست خطوط](../05-settings/02-line.md)                              | `getLineNumbers`             | `getLines`                     | `getLineNumbers`           | `GetLinesAsync`                    | `get_line_numbers`               |

> ستون‌هایی که «در README مستند نشده» ذکر شده‌اند، به این معنا نیست که آن قابلیت در پکیج وجود ندارد؛ صرفاً در فایل README مخزن مربوطه، متد معادل آن به‌صراحت ذکر نشده است. برای اطمینان، به سورس‌کد پکیج یا Issues مخزن مراجعه کنید.

## لایسنس و پشتیبانی

تمام پکیج‌های فوق به‌صورت متن‌باز (عمدتاً با مجوز MIT) در گیت‌هاب سازمان [IPeCompany](https://github.com/IPeCompany) نگهداری می‌شوند. برای گزارش باگ یا درخواست قابلیت جدید، بخش Issues همان مخزن مناسب‌ترین مسیر است؛ برای پرسش‌های مربوط به خود وب‌سرویس (کلید API، اعتبار، خطوط و ...) با پشتیبانی sms.ir در تماس باشید.

---

[بازگشت به فهرست مطالب](../README.md)
