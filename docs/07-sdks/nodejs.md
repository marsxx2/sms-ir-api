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

ارسال یک متن پیامک به گروهی از شماره‌موبایل‌ها — معادل [3.1. ارسال گروهی](../03-sends/01-bulk.md).

```js
smsir.SendBulk('سلام، این یک پیام آزمایشی است', ['09123456789'], null, line_number)
```

### `SendLikeToLike(MessageTexts, Mobiles, SendDateTime, line_number)`

ارسال چند پیامک متفاوت به چند شماره، به‌صورت نظیر به نظیر — معادل [3.2. ارسال نظیر به نظیر](../03-sends/02-like-to-like.md).

```js
smsir.SendLikeToLike(
  ['سلام علی', 'سلام سارا'],
  ['09121111111', '09122222222'],
  null,
  line_number
)
```

### `deleteScheduled(PackId)`

حذف یک بسته‌ی ارسال زمان‌بندی‌شده که هنوز ارسال نشده — معادل [3.3. حذف ارسال زمان‌بندی شده](../03-sends/03-delete-scheduled.md).

```js
smsir.deleteScheduled(packId)
```

### `SendVerifyCode(Mobile, TemplateId, Parameters)`

ارسال پیامک بر اساس یک قالب از پیش تعریف‌شده (کد تایید، فاکتور و ...) — معادل [3.4. ارسال Verify](../03-sends/04-verify.md).

```js
smsir.SendVerifyCode('09123456789', 100000, [
  { name: 'Code', value: '12345' },
])
```

> ⚠️ این پکیج در README خود متدی برای [3.5. ارسال از طریق URL](../03-sends/05-send-via-url.md) مستند نکرده است.

### `ReportMessage(MessageId)`

دریافت گزارش یک پیامک ارسال‌شده — معادل [4.1. گزارش پیامک](../04-reports/01-send-reports.md).

```js
smsir.ReportMessage(messageId)
```

### `ReportPack(PackId)`

دریافت گزارش پیامک‌های یک مجموعه ارسال — معادل [4.3. گزارش مجموعه ارسال](../04-reports/03-send-pack.md).

```js
smsir.ReportPack(packId)
```

### `ReportToday(pageSize, pageNumber)`

دریافت گزارش ارسال‌های امروز، با صفحه‌بندی (مقدار پیش‌فرض `pageSize`: 10) — معادل [4.4. گزارش ارسال‌های روز](../04-reports/04-send-live.md).

```js
smsir.ReportToday(20, 1)
```

### `ReportArchived(fromDate, toDate, pageSize, pageNumber)`

دریافت گزارش ارسال‌های آرشیو شده در یک بازه‌ی زمانی — معادل [4.5. گزارش ارسال‌های آرشیو شده](../04-reports/05-send-archive.md).

```js
smsir.ReportArchived(fromDateUnix, toDateUnix, 100, 1)
```

### `ReportLatestReceived(count)`

دریافت تازه‌ترین پیامک‌های دریافتی — معادل [4.6. گزارش تازه‌ترین پیامک‌های دریافتی](../04-reports/06-receive-latest.md).

```js
smsir.ReportLatestReceived(50)
```

### `ReportTodayReceived(pageSize, pageNumber)`

دریافت پیامک‌های دریافتی امروز — معادل [4.7. گزارش پیامک‌های دریافتی روز](../04-reports/07-receive-live.md).

```js
smsir.ReportTodayReceived(20, 1)
```

### `ReportArchivedReceived(fromDate, toDate, pageSize, pageNumber)`

دریافت پیامک‌های دریافتی آرشیو شده — معادل [4.8. گزارش پیامک‌های دریافتی آرشیو شده](../04-reports/08-receive-archive.md).

```js
smsir.ReportArchivedReceived(fromDateUnix, toDateUnix, 100, 1)
```

### `getCredit()`

دریافت مقدار اعتبار حساب — معادل [5.1. دریافت مقدار اعتبار فعلی](../05-settings/01-credit.md). طبق آزمایش عملی، مقدار بازگشتی **تعداد پیامک باقی‌مانده** است، نه مبلغ ریالی (به یادداشت بخش ۵.۱ مراجعه کنید).

```js
const credit = await smsir.getCredit()
```

### `getLineNumbers()`

دریافت لیست خطوط فعال حساب — معادل [5.2. دریافت لیست خطوط](../05-settings/02-line.md).

```js
const lines = await smsir.getLineNumbers()
```

## پیوندهای بیشتر

- [CHANGELOG مخزن](https://github.com/IPeCompany/SmsPanelV2.nodejs/blob/master/CHANGELOG.md)
- [صفحه‌ی Issues برای گزارش باگ یا درخواست ویژگی](https://github.com/IPeCompany/SmsPanelV2.nodejs/issues)

---

[بازگشت به فهرست SDKها](README.md) · [بازگشت به فهرست مطالب](../README.md)
