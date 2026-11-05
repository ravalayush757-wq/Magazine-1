const { chromium } = require("playwright");

(async () => {

    const browser = await chromium.launch({
        headless: true
    });

    const page = await browser.newPage({

        viewport: {
            width: 794,
            height: 1123
        },

        deviceScaleFactor: 3

    });

    await page.goto("http://127.0.0.1:8080", {

        waitUntil: "networkidle"

    });

    await page.evaluate(async () => {
        await document.fonts.ready;
    });
    await page.emulateMedia({
        media: "print"
    });
    await page.pdf({

        path: "Royal_Monograph_2.pdf",

        format: "A4",

        printBackground: true,

        preferCSSPageSize: true,

        margin: {

            top: "0mm",
            right: "0mm",
            bottom: "0mm",
            left: "0mm"

        }

    });

    await browser.close();

    console.log("PDF Exported Successfully");

})();