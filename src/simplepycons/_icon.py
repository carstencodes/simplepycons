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


class IconIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "icon"

    @property
    def original_file_name(self) -> "str":
        return "icon.svg"

    @property
    def title(self) -> "str":
        return "ICON"

    @property
    def primary_color(self) -> "str":
        return "#31B8BB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ICON</title>
     <path d="M1.92669
 23.93457c-.93754-.17758-1.70436-.94464-1.88217-1.88241-.31993-1.6878
 1.13237-3.1401 2.82018-2.82018.93754.17781 1.7046.94463 1.8824
 1.88217.31993 1.68804-1.13237 3.14034-2.82041 2.82042zM21.13507
 4.76808c-.93754-.1778-1.7046-.94463-1.8824-1.8824-.31993-1.68805
 1.13284-3.14034 2.82065-2.82019.93777.17805 1.70436.94487 1.88217
 1.88241.31992 1.6878-1.13261 3.1401-2.82042 2.82018zm-9.11415
 1.24226c1.1475 0 2.21912.32347
 3.13017.88292l2.58538-2.58562c-1.59582-1.1877-3.57352-1.89092-5.71555-1.89092-5.29278
 0-9.58347 4.29045-9.58347 9.58323 0 2.14227.70321 4.11997 1.89116
 5.7158l2.58538-2.5854c-.55945-.91105-.88268-1.9829-.88268-3.1304
 0-3.30799 2.68162-5.98961 5.9896-5.98961zm5.10664
 2.85936c.55969.91106.88292 1.98267.88292 3.13018 0 3.30798-2.68162
 5.9896-5.98961 5.9896-1.1475 0-2.21935-.323-3.13041-.88268L6.30508
 19.6922c1.59582 1.18794 3.57352 1.89115 5.71579 1.89115 5.29278 0
 9.58323-4.29045 9.58323-9.58346
 0-2.14227-.70345-4.11974-1.89092-5.7158Z" />
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
