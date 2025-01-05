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


class IntercomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "intercom"

    @property
    def original_file_name(self) -> "str":
        return "intercom.svg"

    @property
    def title(self) -> "str":
        return "Intercom"

    @property
    def primary_color(self) -> "str":
        return "#6AFDEF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Intercom</title>
     <path d="M21 0H3C1.343 0 0 1.343 0 3v18c0 1.658 1.343 3 3
 3h18c1.658 0 3-1.342 3-3V3c0-1.657-1.342-3-3-3zm-5.801
 4.399c0-.44.36-.8.802-.8.44 0 .8.36.8.8v10.688c0
 .442-.36.801-.8.801-.443 0-.802-.359-.802-.801V4.399zM11.2
 3.994c0-.44.357-.799.8-.799s.8.359.8.799v11.602c0
 .44-.357.8-.8.8s-.8-.36-.8-.8V3.994zm-4 .405c0-.44.359-.8.799-.8.443
 0 .802.36.802.8v10.688c0 .442-.36.801-.802.801-.44
 0-.799-.359-.799-.801V4.399zM3.199 6c0-.442.36-.8.802-.8.44 0
 .799.358.799.8v7.195c0 .441-.359.8-.799.8-.443
 0-.802-.36-.802-.8V6zM20.52 18.202c-.123.105-3.086 2.593-8.52
 2.593-5.433
 0-8.397-2.486-8.521-2.593-.335-.288-.375-.792-.086-1.128.285-.334.79-.375
 1.125-.09.047.041 2.693 2.211 7.481 2.211 4.848 0 7.456-2.186
 7.479-2.207.334-.289.839-.25 1.128.086.289.336.25.84-.086
 1.128zm.281-5.007c0 .441-.36.8-.801.8-.441
 0-.801-.36-.801-.8V6c0-.442.361-.8.801-.8.441 0
 .801.357.801.8v7.195z" />
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
