import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parent / "publish_wechat.py"
spec = importlib.util.spec_from_file_location("publish_wechat", SCRIPT)
publish_wechat = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = publish_wechat
spec.loader.exec_module(publish_wechat)


class PublishRenderingTests(unittest.TestCase):
    def test_note_number_renders_as_centered_yellow_box(self):
        html = "<blockquote><p>[!NOTE]<br />\nNo.37</p></blockquote><p>第一段正文</p>"

        rendered = publish_wechat.optimize_for_wechat_html(html, template="viral")

        self.assertNotIn("[!NOTE]", rendered)
        self.assertIn("No.37", rendered)
        self.assertIn("text-align:center", rendered)
        self.assertIn("background:#fff7e6", rendered)
        self.assertIn("border:1px solid #ffe1a6", rendered)
        self.assertNotIn("<blockquote", rendered)

    def test_bare_number_renders_as_centered_yellow_box(self):
        html = "<p>No.38</p><p>第一段正文</p>"

        rendered = publish_wechat.optimize_for_wechat_html(html, template="viral")

        self.assertIn("No.38", rendered)
        self.assertIn("text-align:center", rendered)
        self.assertIn("background:#fff7e6", rendered)

    def test_viral_does_not_cardify_first_body_paragraph_after_number(self):
        html = "<blockquote><p>[!NOTE]<br />\nNo.37</p></blockquote><p>第一段正文</p>"

        rendered = publish_wechat.optimize_for_wechat_html(html, template="viral")

        first_body = rendered.split("第一段正文", 1)[0].rsplit("<p", 1)[-1]
        self.assertNotIn("box-shadow", first_body)
        self.assertNotIn("background:#fff7e6", first_body)


if __name__ == "__main__":
    unittest.main()
