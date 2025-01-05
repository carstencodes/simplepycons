#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class OpensearchIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "opensearch"

    @property
    def original_file_name(self) -> "str":
        return "opensearch.svg"

    @property
    def title(self) -> "str":
        return "OpenSearch"

    @property
    def primary_color(self) -> "str":
        return "#005EB8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OpenSearch</title>
     <path d="M23.1515 8.8125a.8484.8484 0 0 0-.8484.8485c0
 6.982-5.6601 12.6421-12.6421 12.6421a.8485.8485 0 0 0 0
 1.6969C17.5802 24 24 17.5802 24 9.661a.8485.8485 0 0
 0-.8485-.8485Zm-5.121 5.4375c.816-1.3311 1.6051-3.1058
 1.4498-5.5905-.3216-5.1468-4.9832-9.0512-9.3851-8.6281C8.372.1971
 6.6025 1.6017 6.7598 4.1177c.0683 1.0934.6034 1.7386 1.473
 2.2348.8279.4722 1.8914.7713 3.097 1.1104 1.4563.4096 3.1455.8697
 4.4438 1.8265 1.5561 1.1467 2.6198 2.4759 2.2569
 4.9606Zm-16.561-9C.6535 6.581-.1355 8.3558.0197 10.8405c.3216 5.1468
 4.9832 9.0512 9.385 8.6281 1.7233-.1657 3.4927-1.5703
 3.3355-4.0863-.0683-1.0934-.6034-1.7386-1.4731-2.2348-.8278-.4722-1.8913-.7713-3.0969-1.1104-1.4563-.4096-3.1455-.8697-4.4438-1.8265-1.5561-1.1467-2.6198-2.476-2.257-4.9606Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://opensearch.org/trademark-brand-policy'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://opensearch.org/trademark-brand-policy'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
