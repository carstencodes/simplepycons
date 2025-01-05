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


class MaildotcomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "maildotcom"

    @property
    def original_file_name(self) -> "str":
        return "maildotcom.svg"

    @property
    def title(self) -> "str":
        return "mail.com"

    @property
    def primary_color(self) -> "str":
        return "#004788"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>mail.com</title>
     <path d="M18.017-.0085H0V15.66c0 1.4057.96 2.5714 2.2457
 2.9143L24 24.0085V5.9915c.0172-3.3086-2.6743-6-5.9828-6zm3
 15.6685H18V8.7857c0-.6685-.223-2.2285-2.2115-2.2285-1.32
 0-2.28.9085-2.28
 2.2285V15.66h-3.0171V8.7857c0-.6685-.2057-2.2285-2.1943-2.2285-1.3543
 0-2.28.9085-2.28 2.2285V15.66H3V3.6086h5.297c1.5943 0 2.8971.6343
 3.7371 1.6629.8915-1.0286 2.2115-1.6629 3.7372-1.6629 3.2914 0 5.2285
 2.1771 5.2285 5.2457l.0172 6.8057z" />
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
