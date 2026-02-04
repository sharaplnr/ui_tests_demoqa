from playwright.sync_api import Page


class TestPracticeForm:

    def test_registration_without_required_fields(self, page: Page):
        name = "Auto"
        lastname = "Test"
        phone_number = "9991112233"
        gender = "Male"

        page.goto('https://demoqa.com/automation-practice-form')
        page.locator('//input[@id = "firstName"]').fill(name)
        page.locator('//input[@id = "lastName"]').fill(lastname)
        page.locator('//input[@id = "userNumber"]').fill(phone_number)
        page.locator('//label[@for="gender-radio-1"]').check()

        page.locator('//button[@id="submit"]').click()

        table_dict = dict()

        rows = page.locator("tbody tr").all()
        for row in rows:
            cells = row.locator("td").all()
            if len(cells) < 2:
                continue
            key = cells[0].inner_text().strip()
            value = cells[1].inner_text().strip()
            table_dict[key] = value

        assert table_dict["Student Name"] == name + " " + lastname, ""
        assert table_dict["Gender"] == gender
        assert table_dict["Mobile"] == phone_number

