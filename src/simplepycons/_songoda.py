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


class SongodaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "songoda"

    @property
    def original_file_name(self) -> "str":
        return "songoda.svg"

    @property
    def title(self) -> "str":
        return "Songoda"

    @property
    def primary_color(self) -> "str":
        return "#FC494A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Songoda</title>
     <path d="M23.23
 4.917c-1.414-.156-6.227-.945-10.604-4.688a.968.968 0 0 0-1.251
 0C6.997 3.967 2.185 4.76.77 4.917a.435.435 0 0 0-.385.463c.29 3.924
 1.918 14.211 10.998 18.482.39.184.844.184 1.234 0 9.079-4.27
 10.708-14.557 10.998-18.482a.435.435 0 0 0-.385-.463zm-1.704
 2.016c-.581 4.255-2.54 11.442-9.126 14.896a.87.87 0 0 1-.807 0C5.006
 18.373 3.048 11.19 2.47 6.935a.365.365 0 0 1 .285-.404 22.733 22.733
 0 0 0 2.208-.596v3.38c0 .489.402.89.89.89.489 0
 .89-.401.89-.89V5.279a22.335 22.335 0 0 0 4.989-2.87.44.44 0 0 1 .534
 0c3.338 2.556 6.805 3.656 8.975 4.12.186.04.31.217.285.405zm-5.831
 7.812c0 .923-.347 1.671-1.04 2.246-.687.574-1.572.86-2.654.86-1.362
 0-2.407-.37-3.135-1.114-.374-.385-.56-.739-.56-1.063a.771.771 0 0 1
 .28-.584c.185-.175.43-.262.733-.262.355 0 .655.167.9.501.4.55.971.824
 1.71.824.449 0 .81-.099 1.083-.297.344-.251.515-.632.515-1.14
 0-.545-.25-1.021-.75-1.43-.361-.294-.891-.606-1.59-.936-.855-.404-1.501-.86-1.938-1.365-.448-.514-.672-1.158-.672-1.93
 0-1.003.398-1.77 1.196-2.298.599-.404 1.352-.606 2.26-.606.995 0
 1.813.267 2.454.801.407.34.611.686.611 1.04 0
 .27-.137.492-.41.667a1.131 1.131 0 0 1-.627.188c-.36
 0-.623-.124-.785-.374-.291-.454-.71-.681-1.258-.681-.588
 0-.978.24-1.17.718a1.99 1.99 0 0
 0-.14.741c-.005.3.108.591.315.809.297.329.83.683 1.598 1.062.92.454
 1.593.874 2.018 1.258.704.654 1.056 1.442 1.056 2.365z" />
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
