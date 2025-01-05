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


class FuelerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fueler"

    @property
    def original_file_name(self) -> "str":
        return "fueler.svg"

    @property
    def title(self) -> "str":
        return "Fueler"

    @property
    def primary_color(self) -> "str":
        return "#09C9E3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fueler</title>
     <path d="M12 0c1.204 0 2.086 1.932 3.172 2.283 1.126.364
 2.978-.67 3.915.009.946.685.527 2.762 1.216 3.704.682.933 2.8 1.175
 3.165 2.295.353 1.081-1.207 2.51-1.207 3.709 0 1.198 1.56 2.628 1.207
 3.709-.365 1.12-2.483 1.362-3.165 2.295-.69.942-.27 3.02-1.217
 3.704-.937.68-2.789-.355-3.914.01C14.086 22.067 13.204 24 12
 24c-1.204
 0-2.086-1.932-3.172-2.283-1.126-.364-2.978.67-3.915-.009-.946-.685-.527-2.762-1.216-3.704-.682-.933-2.8-1.175-3.165-2.295-.353-1.081
 1.207-2.51 1.207-3.709 0-1.198-1.56-2.628-1.207-3.709.365-1.12
 2.483-1.362 3.166-2.295.688-.942.27-3.02 1.216-3.704.937-.68
 2.789.355 3.914-.01C9.914 1.933 10.796 0 12 0Zm-.199 6.34-3.247
 6.169c-.158.3.065.653.388.654h1.707c.234 0 .44.193.44.445v3.706c0
 .459.603.618.825.218l3.39-6.11c.16-.289-.043-.662-.384-.663l-1.85-.002c-.243
 0-.44-.2-.44-.445V6.549c0-.464-.613-.619-.829-.21Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
