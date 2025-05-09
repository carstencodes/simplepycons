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


class MastodonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mastodon"

    @property
    def original_file_name(self) -> "str":
        return "mastodon.svg"

    @property
    def title(self) -> "str":
        return "Mastodon"

    @property
    def primary_color(self) -> "str":
        return "#6364FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mastodon</title>
     <path d="M23.268
 5.313c-.35-2.578-2.617-4.61-5.304-5.004C17.51.242 15.792 0 11.813
 0h-.03c-3.98 0-4.835.242-5.288.309C3.882.692 1.496 2.518.917 5.127.64
 6.412.61 7.837.661 9.143c.074 1.874.088 3.745.26 5.611.118 1.24.325
 2.47.62 3.68.55 2.237 2.777 4.098 4.96 4.857 2.336.792 4.849.923
 7.256.38.265-.061.527-.132.786-.213.585-.184 1.27-.39
 1.774-.753a.057.057 0 0 0 .023-.043v-1.809a.052.052 0 0
 0-.02-.041.053.053 0 0 0-.046-.01 20.282 20.282 0 0 1-4.709.545c-2.73
 0-3.463-1.284-3.674-1.818a5.593 5.593 0 0 1-.319-1.433.053.053 0 0 1
 .066-.054c1.517.363 3.072.546 4.632.546.376 0 .75 0 1.125-.01
 1.57-.044 3.224-.124 4.768-.422.038-.008.077-.015.11-.024 2.435-.464
 4.753-1.92
 4.989-5.604.008-.145.03-1.52.03-1.67.002-.512.167-3.63-.024-5.545zm-3.748
 9.195h-2.561V8.29c0-1.309-.55-1.976-1.67-1.976-1.23 0-1.846.79-1.846
 2.35v3.403h-2.546V8.663c0-1.56-.617-2.35-1.848-2.35-1.112
 0-1.668.668-1.67 1.977v6.218H4.822V8.102c0-1.31.337-2.35
 1.011-3.12.696-.77 1.608-1.164 2.74-1.164 1.311 0 2.302.5 2.962
 1.498l.638 1.06.638-1.06c.66-.999 1.65-1.498 2.96-1.498 1.13 0
 2.043.395 2.74 1.164.675.77 1.012 1.81 1.012 3.12z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/mastodon/mastodon/blob/7cc
f7a73f1c47a8c03712c39f7c591e837cf6d08/app/javascript/images/logo-symbo'''

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
