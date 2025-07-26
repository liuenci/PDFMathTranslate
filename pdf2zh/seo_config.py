"""SEO配置模块

提供SEO优化所需的meta标签、结构化数据和配置管理功能。
"""

from typing import Dict, Optional


class SEOConfig:
    """SEO配置管理类"""
    
    def __init__(self):
        self.default_keywords = [
            "PDF translation", "math formula", "AI translator", "online PDF translator",
            "preserve formatting", "mathematical equations", "document translation",
            "PDF翻译", "数学公式", "在线翻译工具", "格式保持", "文档翻译"
        ]
        
        self.descriptions = {
            "en": "AI-powered PDF translation tool that preserves mathematical formulas, layouts, and formatting. Translate PDF documents while maintaining document structure integrity.",
            "zh": "AI驱动的PDF翻译工具，保持数学公式、布局和格式。在保持文档结构完整性的同时翻译PDF文档。"
        }
        
        self.titles = {
            "en": "PDFMathTranslate - AI PDF Translation Tool | Math Formula Preservation | Free Online PDF Translator",
            "zh": "PDFMathTranslate - AI PDF翻译工具 | 数学公式保持 | 免费在线PDF翻译器"
        }
    
    def get_meta_tags(self, lang: str = "en") -> str:
        """获取SEO meta标签"""
        description = self.descriptions.get(lang, self.descriptions["en"])
        keywords = ", ".join(self.default_keywords)
        
        return f'''
    <!-- SEO Meta Tags -->
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta name="robots" content="index, follow">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="UTF-8">
    <meta name="author" content="PDFMathTranslate Team">
    <meta name="language" content="{lang}">
    
    <!-- Open Graph Tags -->
    <meta property="og:title" content="{self.titles.get(lang, self.titles['en'])}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://pdf2zh.com">
    <meta property="og:site_name" content="PDFMathTranslate">
    <meta property="og:locale" content="{'en_US' if lang == 'en' else 'zh_CN'}">
    
    <!-- Twitter Card Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{self.titles.get(lang, self.titles['en'])}">
    <meta name="twitter:description" content="{description}">
    
    <!-- Additional SEO Tags -->
    <meta name="theme-color" content="#2563eb">
    <meta name="application-name" content="PDFMathTranslate">
    <link rel="canonical" href="https://pdf2zh.com">
        '''
    
    def get_structured_data(self, lang: str = "en") -> str:
        """获取结构化数据JSON-LD"""
        description = self.descriptions.get(lang, self.descriptions["en"])
        
        return f'''
    <!-- Structured Data -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "PDFMathTranslate",
        "description": "{description}",
        "url": "https://pdf2zh.com",
        "applicationCategory": "Productivity",
        "operatingSystem": "Web Browser",
        "offers": {{
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD"
        }},
        "creator": {{
            "@type": "Organization",
            "name": "PDFMathTranslate Team"
        }},
        "featureList": [
            "Preserve mathematical equations",
            "Maintain document formatting",
            "Multiple translation services",
            "Batch processing"
        ]
    }}
    </script>
        '''
    
    def get_comprehensive_head_content(self, existing_head: str = "", lang: str = "en") -> str:
        """获取完整的head内容，合并SEO标签和现有内容"""
        meta_tags = self.get_meta_tags(lang)
        structured_data = self.get_structured_data(lang)
        
        return f"""
{meta_tags}
{structured_data}
{existing_head}
        """
    
    def get_seo_title(self, lang: str = "en") -> str:
        """获取SEO优化的页面标题"""
        return self.titles.get(lang, self.titles["en"])