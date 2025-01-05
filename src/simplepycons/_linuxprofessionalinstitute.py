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


class LinuxProfessionalInstituteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "linuxprofessionalinstitute"

    @property
    def original_file_name(self) -> "str":
        return "linuxprofessionalinstitute.svg"

    @property
    def title(self) -> "str":
        return "Linux Professional Institute"

    @property
    def primary_color(self) -> "str":
        return "#FDC300"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Linux Professional Institute</title>
     <path d="M12-.0002c-6.6273 0-12 5.3728-12 11.9997 0 6.627 5.3727
 12.0007 12 12.0007s12-5.3728 12-12.0007S18.627-.0002 12-.0002Zm0
 20.987c-4.9632 0-8.987-4.0231-8.987-8.9866 0-4.9635 4.0238-8.9867
 8.987-8.9867 4.9632 0 8.987 4.0235 8.987 8.9867 0 4.9631-4.0238
 8.9867-8.987 8.9867zm5.1043-3.0031.7995-2.9975h-7.1631L13.5062
 4.495h-2.9978L6.9118 17.9837Zm.2896-10.4938c0 .8225-.6697
 1.4938-1.4938 1.4938s-1.4897-.6716-1.4897-1.4938c0-.8223.6675-1.4907
 1.4897-1.4907s1.4938.6688 1.4938 1.4907" />
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
