# Events Page Test Cases

---

## TC-01: Verify Events Page Display

**Preconditions:**

* The user has internet access
* A web browser is open

### Test Steps

| Step | Action                   | Data                                 | Expected Result                 |
| ---- | ------------------------ | ------------------------------------ | ------------------------------- |
| 1    | Open the browser         | —                                    | The browser is opened           |
| 2    | Navigate to the link     | https://www.greencity.cx.ua/#/events | The Events page is opened       |
| 3    | Check the list of events | —                                    | The list of events is displayed |

---

## TC-02: Verify Navigation to Event Details

**Preconditions:**

* The user is on the Events page
* At least one event is available in the list

### Test Steps

| Step | Action                    | Data        | Expected Result                  |
| ---- | ------------------------- | ----------- | -------------------------------- |
| 1    | Open the Events page      | URL Events  | The list of events is displayed  |
| 2    | Click "More" on any event | First event | The event details page is opened |
| 3    | Check event details       | —           | Event information is displayed   |

---

## TC-03: Verify Event Search Functionality

**Preconditions:**

* The user is on the Events page

### Test Steps

| Step | Action                         | Data       | Expected Result                      |
| ---- | ------------------------------ | ---------- | ------------------------------------ |
| 1    | Open the Events page           | URL Events | The page is displayed                |
| 2    | Enter text in the search field | s          | Relevant events are displayed        |
| 3    | Clear the search field         | —          | The full list of events is displayed |

---

## TC-04: Verify Search with More Than One Character

**Preconditions:**

* The user is on the Events page
* There are events matching the search query

### Test Steps

| Step | Action                        | Data       | Expected Result               |
| ---- | ----------------------------- | ---------- | ----------------------------- |
| 1    | Open the Events page          | URL Events | The page is displayed         |
| 2    | Enter one character in search | s          | Relevant events are displayed |
| 3    | Enter more than one character | som        | Relevant events are displayed |

---
