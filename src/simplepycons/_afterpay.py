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


class AfterpayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "afterpay"

    @property
    def original_file_name(self) -> "str":
        return "afterpay.svg"

    @property
    def title(self) -> "str":
        return "Afterpay"

    @property
    def primary_color(self) -> "str":
        return "#B2FCE4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Afterpay</title>
     <path d="M12 0C5.373 0 0 5.373 0 12c0 6.628 5.373 12 12 12 6.628
 0 12-5.372 12-12 0-6.627-5.372-12-12-12Zm1.236 4.924a2.21 2.21 0 0 1
 1.15.299l4.457 2.557c1.495.857 1.495 3.013 0 3.87l-4.457
 2.558c-1.488.854-3.342-.22-3.342-1.935v-.34a.441.441 0 0
 0-.66-.383L6.287 13.9a.441.441 0 0 0 0 .765l4.096 2.35a.44.44 0 0 0
 .661-.382v-.685c0-.333.36-.542.649-.376l1.041.597a.441.441 0 0 1
 .222.383v.29c0 1.715-1.854 2.789-3.342 1.935L5.157
 16.22c-1.495-.857-1.495-3.013 0-3.87l4.457-2.558c1.488-.854 3.342.22
 3.342 1.935v.34c0 .34.366.551.66.383l4.097-2.35a.441.441 0 0 0
 0-.765l-4.096-2.351a.441.441 0 0 0-.661.382v.685c0
 .333-.36.541-.649.375l-1.041-.597a.442.442 0 0
 1-.222-.383v-.29c0-1.285 1.043-2.21 2.192-2.233z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.afterpay.com/en-AU/business/resou'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.afterpay.com/en-AU/business/resou'''

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
