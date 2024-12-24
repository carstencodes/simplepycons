#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class NapsterIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "napster"

    @property
    def original_file_name(self) -> "str":
        return "napster.svg"

    @property
    def title(self) -> "str":
        return "Napster"

    @property
    def primary_color(self) -> "str":
        return "#2259FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Napster</title>
     <path d="M20.495 4.543c-.22 0-.438
 0-.657.03h-.031l-.032-.03C17.93 2.21 15.02.798 12.015.798c-3.004
 0-5.945 1.412-7.76
 3.775l-.031.03h-.031c-.22-.03-.439-.03-.658-.03H2.16v2.394l-.032.03A3.628
 3.628 0 0 0 0 10.282c0 1.412.844 2.701 2.127 3.284h.063v.062c.031
 5.278 4.443 9.575 9.825 9.575s9.794-4.297
 9.825-9.575v-.062l.032-.03C23.155 12.92 24 11.632 24
 10.25c0-1.412-.845-2.7-2.128-3.284l-.032-.03V4.542zM6.821 5.34a7.443
 7.443 0 0 1 5.194-2.117c1.94 0 3.818.767 5.195
 2.117l.062.062-.094.061c-.375.215-.72.43-1.064.675l-.03.031-.032-.03c-.908-.461-2.347-.983-4.005-.983s-3.098.522-4.006.982l-.03.031-.032-.03a10.22
 10.22 0 0 0-1.064-.676l-.188-.061zm12.329 8.195c0 3.866-3.223
 7.027-7.166 7.027-3.942
 0-7.134-3.16-7.134-7.027V7.458l.094.03c1.252.308 2.44 1.658 2.722
 1.996.313-.338 1.784-1.658 4.35-1.658 2.565 0 4.036 1.35 4.35
 1.658.28-.338 1.438-1.688 2.721-1.995l.094-.031v6.077z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.napster.com/us/wp-content/uploads'''

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
