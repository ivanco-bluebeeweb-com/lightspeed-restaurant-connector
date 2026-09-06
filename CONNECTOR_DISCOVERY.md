# Lightspeed Restaurant Connector — Discovery

**Vendor:** Lightspeed Restaurant (https://lightspeedhq.com/pos/restaurant)  
**API Base URL:** `https://api.lightspeed.app`  
**Authentication:** OAuth 2.0 Authorization Code Grant

## Архитектура API
- **Ключевые сущности:** заказы (/orders), чеки (/receipts), меню и группы блюд (/menus), залы и столы (/floors, /tables)
- **Формат обмена данными:** JSON / HTTPS REST.
- **Обработка ошибок:** Стандартные HTTP-коды (400, 401, 403, 404, 429, 500) с типизацией ответа.
- **Тестовая точка проверки подключения:** `GET /v1/account`.
