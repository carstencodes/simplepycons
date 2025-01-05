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


class XenditIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "xendit"

    @property
    def original_file_name(self) -> "str":
        return "xendit.svg"

    @property
    def title(self) -> "str":
        return "Xendit"

    @property
    def primary_color(self) -> "str":
        return "#4573FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Xendit</title>
     <path d="M11.781 2.743H7.965l-5.341 9.264 5.341 9.263-1.312
 2.266L0 12.007 6.653.464h6.454l-1.326 2.279Zm-5.128 2.28
 1.312-2.28L9.873 6.03 8.561 8.296 6.653 5.023Zm9.382-2.28 1.312
 2.28L7.965 21.27l-1.312-2.279 9.382-16.248Zm-5.128 20.793
 1.298-2.279h3.83L14.1 17.931l1.312-2.267 1.926 3.337
 4.038-6.994-5.341-9.264L17.347.464 24 12.007l-6.653 11.529h-6.44Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.xendit.co/en/company/asset-and-br'''

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
