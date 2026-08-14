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

ارسال یک متن به چند شماره‌موبایل — معادل [3.1. ارسال گروهی](../03-sends/01-bulk.md).

```python
sms_ir.send_bulk_sms(numbers, message, linenumber)
```

### `send_like_to_like(numbers, messages, linenumber, send_date_time)`

ارسال نظیر به نظیر — معادل [3.2. ارسال نظیر به نظیر](../03-sends/02-like-to-like.md).

```python
sms_ir.send_like_to_like(numbers, messages, linenumber, send_date_time)
```

### `delete_scheduled(pack_id)`

حذف یک بسته‌ی ارسال زمان‌بندی‌شده — معادل [3.3. حذف ارسال زمان‌بندی شده](../03-sends/03-delete-scheduled.md).

```python
sms_ir.delete_scheduled(pack_id)
```

### `send_verify_code(number, template_id, parameters)`

ارسال پیامک بر اساس قالب از پیش تعریف‌شده — معادل [3.4. ارسال Verify](../03-sends/04-verify.md).

```python
sms_ir.send_verify_code(
    number="+989111111111",
    template_id=10000,
    parameters=[
        {"name": "code", "value": 12345},
    ],
)
```

> ⚠️ این پکیج در README خود متدی برای [3.5. ارسال از طریق URL](../03-sends/05-send-via-url.md) مستند نکرده است.

### `report_message(message_id)`

گزارش یک پیامک ارسال‌شده — معادل [4.1. گزارش پیامک](../04-reports/01-send-reports.md).

```python
sms_ir.report_message(message_id)
```

> ⚠️ این پکیج در README خود متد مجزایی برای [4.2. گزارش مجموعه ارسال‌های روز](../04-reports/02-live-pack.md) (لیست پک‌ها) مستند نکرده است.

### `report_pack(pack_id)`

گزارش یک مجموعه‌ی ارسال — معادل [4.3. گزارش مجموعه ارسال](../04-reports/03-send-pack.md).

```python
sms_ir.report_pack(pack_id)
```

### `report_today(page_size, page_number)`

گزارش ارسال‌های امروز — معادل [4.4. گزارش ارسال‌های روز](../04-reports/04-send-live.md).

```python
sms_ir.report_today(page_size, page_number)
```

### `report_archived(from_date, to_date, page_size, page_number)`

گزارش ارسال‌های آرشیو شده — معادل [4.5. گزارش ارسال‌های آرشیو شده](../04-reports/05-send-archive.md).

```python
sms_ir.report_archived(from_date, to_date, page_size, page_number)
```

### `report_latest_received(count)`

آخرین پیامک‌های دریافتی — معادل [4.6. گزارش تازه‌ترین پیامک‌های دریافتی](../04-reports/06-receive-latest.md).

```python
sms_ir.report_latest_received(count)
```

### `report_today_received(page_size, page_number)`

پیامک‌های دریافتی امروز — معادل [4.7. گزارش پیامک‌های دریافتی روز](../04-reports/07-receive-live.md).

```python
sms_ir.report_today_received(page_size, page_number)
```

### `report_archived_received(from_date, to_date, page_size, page_number)`

پیامک‌های دریافتی آرشیو شده — معادل [4.8. گزارش پیامک‌های دریافتی آرشیو شده](../04-reports/08-receive-archive.md).

```python
sms_ir.report_archived_received(from_date, to_date, page_size, page_number)
```

### `get_credit()`

دریافت مقدار اعتبار حساب — معادل [5.1. دریافت مقدار اعتبار فعلی](../05-settings/01-credit.md). طبق آزمایش عملی، مقدار بازگشتی **تعداد پیامک باقی‌مانده** است، نه مبلغ ریالی (به یادداشت بخش ۵.۱ مراجعه کنید).

```python
sms_ir.get_credit()
```

### `get_line_numbers()`

دریافت لیست خطوط فعال — معادل [5.2. دریافت لیست خطوط](../05-settings/02-line.md).

```python
sms_ir.get_line_numbers()
```

## پیوندهای بیشتر

- [صفحه‌ی Issues برای گزارش باگ یا درخواست ویژگی](https://github.com/IPeCompany/SmsPanelV2.Python/issues)
- [پکیج در PyPI](https://pypi.org/project/smsir-python/)

---

[بازگشت به فهرست SDKها](README.md) · [بازگشت به فهرست مطالب](../README.md)
