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


class PaperlessngxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "paperlessngx"

    @property
    def original_file_name(self) -> "str":
        return "paperlessngx.svg"

    @property
    def title(self) -> "str":
        return "Paperless-ngx"

    @property
    def primary_color(self) -> "str":
        return "#17541F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Paperless-ngx</title>
     <path d="M6.338
 23.028c-.117-.56-.353-1.678-.382-1.678-4.977-2.975-4.388-8.128-2.739-11.073.353
 3.71 6.92 6.273 3.092 10.808-.03.059.177.765.353 1.413.766-1.296
 1.915-2.856 1.856-3.004C3.806 8.01 18.53 7.126 21.592 0c1.385
 6.89-.706 17.55-12.544 20.26-.06.03-2.15 3.71-2.238 3.74
 0-.059-.884-.03-.766-.324.059-.177.177-.412.294-.648zm-.147-2.768c1.502-1.737-.265-4.712-1.325-5.683
 1.796 3.092 1.679 4.888 1.325 5.683z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/paperless-ngx/paperless-ng
x/blob/e16645b146da24f07004eb772a455450354a37a7/resources/logo/web/svg'''

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
